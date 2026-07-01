import json
from utils import _is_valid_grade, _is_valid_studentID


def _load_students():
    try:
        with open("data/students.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("students record unavailable at the moment")
        return False


def _load_grades():
    try:
        with open("data/grades.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"grades": []}


def _save_grades(data):
    with open("data/grades.json", "w") as file:
        json.dump(data, file, indent=4)

    data = _load_students()
    if not data:
        print("oops..try again later")

    for student in data["students"]:
        if student["id"] == id:
            return True

    return False


def view_student_grades(student_id):
    if not _is_valid_studentID(student_id):
        print("invalid student ID entered")
        return False

    data = _load_grades()

    if not data["grades"]:
        print("student grades dont exist")
        return False

    print('\n')
    for grades in data["grades"]:
        if grades["student_id"] == student_id:
            print("Student ID:", grades["student_id"])
            for k, v in grades["grades"].items():
                print(k, v, "marks")
            return True

    print("no student found")
    return False


def assign_grade(student_id, course_name, grade):
    if not _is_valid_grade(grade):
        print("invalid grade entered")
        return

    if not _is_valid_studentID(student_id):
        print("invalid student id entered")
        return

    data = _load_grades()

    if not data["grades"]:
        print("no grades exist for any student")
        return

    for grades in data["grades"]:
        if grades["student_id"] == student_id:
            gr = grades["grades"]

            if course_name not in gr:
                print("course doesnt exist")
                return

            if gr[course_name] == "None":
                gr[course_name] = grade
                _save_grades(data)
                print("grade assigned")
                return
            else:
                print("grade already assigned")
                return

    print("student id doesnt exist")
    return


def update_grade(student_id, course_name, grade):
    if not _is_valid_grade(grade):
        print("invalid grade entered")
        return

    if not _is_valid_studentID(student_id):
        print("invalid student id entered")
        return

    data = _load_grades()

    if not data["grades"]:
        print("no grades exist for any student")
        return

    for grades in data["grades"]:
        if grades["student_id"] == student_id:
            gr = grades["grades"]

            if course_name not in gr:
                print("course doesnt exist")
                return

            if gr[course_name] != "None":
                gr[course_name] = grade
                _save_grades(data)
                print("grade updated")
                return
            else:
                print("cannot update, assign first")
                return

    print("student ID doesnt exist")
    return
