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
        print("student grades dont exist")
        return

    for grades in data["grades"]:
        if grades["student_id"] == student_id:
            print(grades)
            return

    print('no student found')
    return None


def assign_grade(student_id, course_name, grade):
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
    data = _load_grades()

    if not data["grades"]:
        print("no grades exist for any student")
        return

    if view_student_grades(student_id) is not None:

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
    else:
        print("no student found for this ID")
        return
