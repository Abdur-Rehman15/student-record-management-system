from dataclasses import dataclass
from functools import wraps
from datetime import datetime
import json

def my_logger(orig_func):
    import logging

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.basicConfig(
            filename=f"{orig_func.__name__}.log", level=logging.INFO, force=True
        )

        logging.info(f"new student added with args: {args} and kwargs: {kwargs} at this time: {datetime.now()}")
        return orig_func(*args, **kwargs)

    return wrapper

@dataclass
class Student:
    id: int
    name: str
    age: int
    email_address: str
    department: str

    @classmethod
    def _load_data(cls):
        try:
            with open("data/students.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {"students": []}

    @classmethod
    def _save_data(cls, data):
        with open("data/students.json", "w") as file:
            json.dump(data, file, indent=4)


    # ----------add student-------------
    @classmethod
    @my_logger
    def add_student(
        cls, id: int, name: str, age: int, email_address: str, department: str
    ):
        new_student = {
            "id": id,
            "name": name,
            "age": age,
            "email_address": email_address,
            "department": department,
        }

        data = cls._load_data()
        data["students"].append(new_student)
        cls._save_data(data)

        print("student added successfully")
        return

    # ----------update student-------------
    @classmethod
    def update_student(
        cls, name: str, id: int, email_address: str, age: int, department: str
    ):
        data = cls._load_data()

        if not data["students"]:
            print("no student exists")
            return

        for student in data["students"]:
            if student["id"] == id:
                student["name"] = name
                student["age"] = age
                student["email_address"] = email_address
                student["department"] = department
                
                cls._save_data(data)
                print("students details updated")
                return
                
        print("student not found")
        return

    @classmethod
    def get_all_students(cls):
        data = cls._load_data()
        
        if not data["students"]:
            print("no student exists")
            return

        for student in data["students"]:
            yield student

    # ----------search student by ID-------------
    @classmethod
    def search_student_by_ID(cls, id: int):
        data = cls._load_data()

        for student in data["students"]:
            if student["id"] == id:
                print(student)
                return

        print("no student exists with this ID")
        return

    # ----------delete student-------------
    @classmethod
    def delete_student(cls, id: int):
        data = cls._load_data()

        updated_list = {"students": []}
        student_found = False

        for student in data["students"]:
            if student["id"] != id:
                updated_list["students"].append(student)
            else:
                student_found = True

        if not student_found:
            print("no student exists with this ID")
            return

        cls._save_data(updated_list)
        print("student deleted successfully")
        return
