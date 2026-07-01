import json

# ===========error handling krni he course ids wgera ki abhi=========

def _load_enrollments():
    try:
        with open("data/enrollments.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"enrollments": []}


def _save_enrollments(data):
    with open("data/enrollments.json", "w") as file:
        json.dump(data, file, indent=4)


# ----------new enrollment in course------------
def enroll_student_in_course(student_id, course_id):
    new_enrollment = {"student_id": student_id, "course_id": course_id}

    data = _load_enrollments()

    for enrollment in data["enrollments"]:
        if enrollment["student_id"] == student_id:
            if course_id in enrollment["course_id"]:
                print("Student already enrolled in this course")
                return

            enrollment["course_id"].append(course_id)
            _save_enrollments(data)
            print("student enrolled successfully in the course")
            return

    data["enrollments"].append(new_enrollment)
    _save_enrollments(data)
    print("student enrolled successfully in the course")
    return


# ----------view enrolled courses------------
def view_enrolled_courses(student_id):
    data = _load_enrollments()

    if "enrollments" not in data or not data["enrollments"]:
        print("no enrollments exist")
        return

    for enrollment in data["enrollments"]:
        if enrollment["student_id"] == student_id:
            print('Student with ID:', enrollment["student_id"], 'is enrolled in course(s) with ID:', enrollment["course_id"])
            return

    print("no enrollments found for this student")
    return


# --------remove enrollment from course--------------
def remove_enrollment_from_course(student_id, course_id):
    data = _load_enrollments()

    if "enrollments" not in data or not data["enrollments"]:
        print("no enrollments exist")
        return

    updated_list = {"enrollments": []}
    for enrollment in data["enrollments"]:
        if enrollment["student_id"] == student_id:
            new_list = []
            for id in enrollment["course_id"]:
                if id != course_id:
                    new_list.append(id)
            enrollment["course_id"] = new_list

        updated_list["enrollments"].append(enrollment)

    _save_enrollments(updated_list)

    print("enrollment removed successfully")
    return
