import json


def load_students():
    try:

        with open("data/students.json", "r") as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        open("data/students.json", "w")
        return None


def load_courses():
    try:

        with open("data/courses.json", "r") as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        open("data/courses.json", "w")
        return None


def load_enrollments():
    try:

        with open("data/enrollments.json", "r") as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        open("data/enrollments.json", "w")
        return None


def load_grades():
    try:

        with open("data/grades.json", "r") as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        open("data/grades.json", "w")
        return None
