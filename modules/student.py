from dataclasses import dataclass
from functools import wraps
from datetime import datetime
from utils import _is_valid_studentID, _is_existing_student, _is_valid_age
import json


def my_logger(orig_func):
    import logging

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.basicConfig(
            filename=f"{orig_func.__name__}.log", level=logging.INFO, force=True
        )

        logging.info(
            f"new student added with args: {args} and kwargs: {kwargs} at this time: {datetime.now()}"
        )
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
        if not _is_valid_studentID(id):

            print("student id is not valid")
            return

        if not _is_valid_age(age):
            print("age not valid")
            return

        data = cls._load_data()
        if not _is_existing_student(data, id):

            new_student = {
                "id": id,
                "name": name,
                "age": age,
                "email_address": email_address,
                "department": department,
            }

            data["students"].append(new_student)
            cls._save_data(data)

            print("student added successfully")
            return
        else:
            print("student already exists")

    # ----------update student-------------
    @classmethod
    def update_student(
        cls, name: str, id: int, email_address: str, age: int, department: str
    ):
        if not _is_valid_studentID(id):

            print("student id is not valid")
            return

        if not _is_valid_age(age):
            print("age not valid")
            return

        data = cls._load_data()
        if _is_existing_student(data, id):

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

        else:
            print("student not found")
            return

    # ----------get all students-------------
    @classmethod
    def get_all_students(cls):
        data = cls._load_data()

        if not data["students"]:
            print("no student exists")
            return

        print("\n")
        for student in data["students"]:
            yield student

    # ----------search student by ID-------------
    @classmethod
    def search_student_by_ID(cls, id: int):
        if not _is_valid_studentID(id):

            print("student id is not valid")
            return

        data = cls._load_data()
        if _is_existing_student(data, id):

            for student in data["students"]:
                if student["id"] == id:
                    print(student)
                    return

        else:
            print("no student exists with this ID")
            return

    # ----------delete student-------------
    @classmethod
    def delete_student(cls, id: int):
        if not _is_valid_studentID(id):

            print("student id is not valid")
            return

        data = cls._load_data()
        if _is_existing_student(data, id):

            updated_list = {"students": []}

            for student in data["students"]:
                if student["id"] != id:
                    updated_list["students"].append(student)

            cls._save_data(updated_list)
            print("student deleted successfully")
            return
        else:
            print("no student exists with this ID")
            return
