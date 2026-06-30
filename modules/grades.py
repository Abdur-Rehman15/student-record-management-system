import json


def assign_grade(student_id, course_name, grade):
    try:

        with open("data/grades.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        print("no course exists like that")

    for grades in data:
        if grades["student_id"] == student_id:
            gr = grades["grades"]
            if (gr[course_name]) == "None":
                gr[course_name] = grade
                print("grade assigned")
            else:
                print("grade already assigned")

    with open("data/grades.json", "w") as file:
        json.dump(data, file, indent=4)


def update_grade(student_id, course_name, grade):
    try:

        with open("data/grades.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        print("no course exists like that")

    for grades in data:
        if grades["student_id"] == student_id:
            gr = grades["grades"]
            if (gr[course_name]) != "None":
                gr[course_name] = grade
                print("grade updated")
            else:
                print("grade already assigned")

    with open("data/grades.json", "w") as file:
        json.dump(data, file, indent=4)


def view_student_grades(student_id):
    try:

        with open("data/grades.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        print("no course exists like that")

    for grades in data:
        if grades["student_id"] == student_id:
            print(grades)
