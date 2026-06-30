import json


def _load_grades():
    try:
        with open("data/grades.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"grades": []}


def _save_grades(data):
    with open("data/grades.json", "w") as file:
        json.dump(data, file, indent=4)


def view_student_grades(student_id):
    data = _load_grades()

    if not data["grades"]:
        return "student grades dont exist"

    for grades in data["grades"]:
        if grades["student_id"] == student_id:
            return grades

    return None


def assign_grade(student_id, course_name, grade):
    data = _load_grades()

    if not data["grades"]:
        return "no grades exist for any student"

    for grades in data["grades"]:
        if grades["student_id"] == student_id:
            gr = grades["grades"]
            
            if course_name not in gr:
                return "course doesnt exist"
                
            if gr[course_name] == "None":
                gr[course_name] = grade
                _save_grades(data)
                return "grade assigned"
            else:
                return "grade already assigned"

    return "student id doesnt exist"


def update_grade(student_id, course_name, grade):
    data = _load_grades()

    if not data["grades"]:
        return "no grades exist for any student"

    for grades in data["grades"]:
        if grades["student_id"] == student_id:
            gr = grades["grades"]
            
            if course_name not in gr:
                return "course doesnt exist"
                
            if gr[course_name] != "None":
                gr[course_name] = grade
                _save_grades(data)
                return "grade updated"
            else:
                return "cannot update, assign first"

    return "student ID doesnt exist"
