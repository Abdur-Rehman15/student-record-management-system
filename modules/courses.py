from dataclasses import dataclass
import json


@dataclass
class Course:
    name: str
    id: int
    credit_hrs: int

    # ------------add course--------------
    @classmethod
    def add_course(cls, name: str, id: int, credit_hrs: int):

        new_course = {"name": name, "id": id, "credit_hrs": credit_hrs}

        try:

            with open("data/courses.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            data = {"courses": []}

        for courses in data["courses"]:
            if courses["id"] == id:
                return "course already exists"

        data["courses"].append(new_course)

        with open("data/courses.json", "w") as file:
            json.dump(data, file, indent=4)

        return "new course added successfully"

    # ------------delete course------------
    @classmethod
    def delete_course(cls, id: int):
        try:

            with open("data/courses.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            print("course not exists")

        updated_course_list = {"courses": []}
        for courses in data["courses"]:
            if courses["id"] != id:
                updated_course_list["courses"].append(courses)

        with open("data/courses.json", "w") as file:
            json.dump(updated_course_list, file, indent=4)

        return "course deleted successfully"

    # ----------view all courses-------------
    @classmethod
    def view_all_courses(cls):
        try:

            with open("data/courses.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            return "no course exists"

        if data is None:
            return "no course added"

        return data
