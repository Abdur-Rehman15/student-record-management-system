from dataclasses import dataclass
import json


@dataclass
class Student:
    id: int
    name: str
    age: int
    email_address: str
    department: str

    # ---------- Helper Methods ----------
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

    # ----------update student-------------
    @classmethod
    def update_student(
        cls, name: str, id: int, email_address: str, age: int, department: str
    ):
        data = cls._load_data()

        if not data["students"]:
            return "no student exists"

        for student in data["students"]:
            if student["id"] == id:
                student["name"] = name
                student["age"] = age
                student["email_address"] = email_address
                student["department"] = department
                
                cls._save_data(data)
                return "students details updated"
                
        return "student not found"

    @classmethod
    def get_all_students(cls):
        data = cls._load_data()
        
        if not data["students"]:
            return "no student exists"

        return data

    # ----------search student by ID-------------
    @classmethod
    def search_student_by_ID(cls, id: int):
        data = cls._load_data()

        for student in data["students"]:
            if student["id"] == id:
                return student

        return "no student exists with this ID"

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
            return "no student exists with this ID"

        cls._save_data(updated_list)
        return "student deleted successfully"
