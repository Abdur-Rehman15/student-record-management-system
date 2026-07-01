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
                print("course already exists")
                return

        data["courses"].append(new_course)

        cls._save_data(data)

        print("new course added successfully")
        return

    # ------------delete course------------
    @classmethod
    def delete_course(cls, id: int):
        data = cls._load_data()
        isFound=False

        updated_course_list = {"courses": []}
        for courses in data["courses"]:
            if courses["id"] == id:
                isFound=True
                continue
            updated_course_list["courses"].append(courses)

        cls._save_data(updated_course_list)

        if isFound==True:
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
