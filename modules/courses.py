from dataclasses import dataclass
from utils import _is_valid_courseID, _is_existing_courseID
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

        if not _is_valid_courseID(id):
            print("invalid course id entered")
            return

        data = cls._load_data()
        if not _is_existing_courseID(data, id):

            new_course = {"name": name, "id": id, "credit_hrs": credit_hrs}


            for courses in data["courses"]:
                if courses["id"] == id:
                    print("course already exists")
                    return

            data["courses"].append(new_course)

            cls._save_data(data)

            print("new course added successfully")
            return
        
        else:
            print('course id already exists')
            return

    # ------------delete course------------
    @classmethod
    def delete_course(cls, id: int):

        if not _is_valid_courseID(id):
            print("invalid course id entered")
            return
        
        data = cls._load_data()
        if _is_existing_courseID(data, id):

            updated_course_list = {"courses": []}
            for courses in data["courses"]:
                if courses["id"] != id:
                    updated_course_list["courses"].append(courses)

            cls._save_data(updated_course_list)
            print("course deleted successfully")

        else:
            print('No course found against this ID')
        return
            

    # ----------view all courses-------------
    @classmethod
    def view_all_courses(cls):
        data = cls._load_data()

        if data is None:
            print("no course added")
            return

        for course in data["courses"]:
            yield course
        return
