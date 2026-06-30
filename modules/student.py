from dataclasses import dataclass
import json


@dataclass
class Student:
    name: str
    id: int
    email_address: str
    age: int
    department: str

    #  abhi yahan pr student details bhi validate krni hain

    # ----------add student-------------
    def add_student(
        self, name: str, id: int, email_address: str, age: int, department: str
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
            data = []

        data.append(new_student)

        with open("data/students.json", "w") as file:
            json.dump(data, file, indent=4)

    # ----------update student-------------
    def update_student(
        self, name: str, id: int, email_address: str, age: int, department: str
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

    def get_all_students(self):
        try:

            with open("data/students.json", "r") as file:
                data = json.load(file)

            print("---All Students---")
            print(data)

        except FileNotFoundError:
            print("no student exists")

    # ----------search student by ID-------------
    def search_student_by_ID(self, id: int):
        try:

            with open("data/students.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            print("no student exists")

        for student in data:
            if student["id"] == id:

                print("---students details---")
                print(student)
                pass

    # ----------delete student-------------
    def delete_student(self, id: int):
        try:

            with open("data/students.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            print("no student exists")

        updated_list = {}
        for student in data:
            if student["id"] != id:
                updated_list.append(student)

        with open("data/students.json", "w") as file:
            json.dump(updated_list, file, indent=4)

        print("student deleted")