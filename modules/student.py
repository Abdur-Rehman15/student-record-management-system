from dataclasses import dataclass
import json


@dataclass
class Student:
    id: int
    name: str
    age: int
    email_address: str
    department: str

    #  abhi yahan pr student details bhi validate krni hain

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

        try:

            with open("data/students.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            data = {"students": []}

        data["students"].append(new_student)

        with open("data/students.json", "w") as file:
            json.dump(data, file, indent=4)

        print("student added successfully")

    # ----------update student-------------
    @classmethod
    def update_student(
        cls, name: str, id: int, email_address: str, age: int, department: str
    ):
        try:

            with open("data/students.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            print("no student exists")

        for student in data:
            if student["id"] == id:

                print("students details updated")
                with open("data/students.json", "w") as file:
                    json.dump(data, file, indent=4)
                pass

    @classmethod
    def get_all_students(cls):
        try:

            with open("data/students.json", "r") as file:
                data = json.load(file)

            print("---All Students---")
            print(data)

        except FileNotFoundError:
            print("no student exists")

    # ----------search student by ID-------------
    @classmethod
    def search_student_by_ID(cls, id: int):
        try:

            with open("data/students.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            return "no student exists"

        for student in data["students"]:
            if student["id"] == id:
                return student

        return "no student exists with this ID"

    # ----------delete student-------------
    @classmethod
    def delete_student(cls, id: int):
        try:

            with open("data/students.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            return "no student exists"

        updated_list = {"students": []}
        for student in data["students"]:
            if student["id"] != id:
                updated_list["students"].append(student)

        with open("data/students.json", "w") as file:
            json.dump(updated_list, file, indent=4)

        return "student deleted successfully"
