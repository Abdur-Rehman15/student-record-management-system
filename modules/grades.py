import json


def view_student_grades(student_id):
    try:

        with open("data/grades.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        return "student grades dont exist"

    for grades in data["grades"]:
        if grades["student_id"] == student_id:
            return grades

    return "no grades found"


def assign_grade(student_id, course_name, grade):
    try:

        with open("data/grades.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        return "no grades exist for any student"

    print(view_student_grades(student_id))

    for grades in data["grades"]:
        if grades["student_id"] == student_id:
            gr = grades["grades"]
            if course_name not in gr:
                return "course doesnt exist"
            if (gr[course_name]) == "None":
                gr[course_name] = grade
                with open("data/grades.json", "w") as file:
                    json.dump(data, file, indent=4)
                return "grade assigned"
            else:
                return "grade already assigned"

    return "student id doesnt exist"


def update_grade(student_id, course_name, grade):
    try:

        with open("data/grades.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        return "no grades exist for any student"

    print(view_student_grades(student_id))

    for grades in data["grades"]:
        if grades["student_id"] == student_id:
            gr = grades["grades"]
            if course_name not in gr:
                return "course doesnt exist"
            if (gr[course_name]) != "None":
                gr[course_name] = grade
                with open("data/grades.json", "w") as file:
                    json.dump(data, file, indent=4)
                return "grade updated"
            else:
                return "grade already assigned"

    return "student ID doesnt exist"
