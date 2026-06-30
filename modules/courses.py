from dataclasses import dataclass
import json


@dataclass
class Course:
    name: str
    id: int
    credit_hrs: int

    @classmethod
    def _load_data(cls):
        try:
            with open("data/courses.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {"courses": []}

    @classmethod
    def _save_data(cls, data):
        with open("data/courses.json", "w") as file:
            json.dump(data, file, indent=4)

    # ------------add course--------------
    @classmethod
    def add_course(cls, name: str, id: int, credit_hrs: int):

        new_course = {"name": name, "id": id, "credit_hrs": credit_hrs}

        data = cls._load_data()

        for courses in data["courses"]:
            if courses["id"] == id:
                return "course already exists"

        data["courses"].append(new_course)

        cls._save_data(data)

        return "new course added successfully"

    # ------------delete course------------
    @classmethod
    def delete_course(cls, id: int):
        data = cls._load_data()

        updated_course_list = {"courses": []}
        for courses in data["courses"]:
            if courses["id"] != id:
                updated_course_list["courses"].append(courses)

        cls._save_data(updated_course_list)

        return "course deleted successfully"

    # ----------view all courses-------------
    @classmethod
    def view_all_courses(cls):
        data = cls._load_data()

        if data is None:
            return "no course added"

        return data
