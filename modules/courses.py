from dataclasses import dataclass
import json


@dataclass
class Course:
    name: str
    id: int
    credit_hrs: int

    def add_course(self, name: str, id: int, credit_hrs: int):

        new_course = {"name": name, "id": id, "credit_hrs": credit_hrs}

        try:

            with open("data/courses.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            data = []

        data.append(new_course)

        with open("data/courses.json", "w") as file:
            json.dump(data, file, indent=4)

    def delete_course(self, id: int):
        try:

            with open("data/courses.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            print("course not exists")

        updated_course_list = {}
        for courses in data:
            if courses["id"] != id:
                updated_course_list.append(courses)

        with open("data/courses.json", "w") as file:
            json.dump(updated_course_list, file, indent=4)

    def view_all_courses(self):
        try:

            with open("data/courses.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            print("no course exists")

        print('---All Courses---')
        print(data)

        
