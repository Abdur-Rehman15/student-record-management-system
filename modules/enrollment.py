import json

# ===========ye sab update krna he abhi course id ki data type change krny ky bad (krdi hui he)==========


# ----------new enrollment in course------------
def enroll_student_in_course(student_id, course_id):
    new_enrollment = {"student_id": student_id, "course_id": course_id}

    try:

        with open("data/enrollments.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        data = []

    data.append(new_enrollment)

    with open("data/enrollments.json", "w") as file:
        json.dump(data, file, indent=4)


# ----------view enrolled courses------------
def view_enrolled_courses(student_id):
    try:

        with open("data/enrollments.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        print("no enrollments exist")

    for enrollment in data:
        if enrollment["student_id"] == student_id:
            print(enrollment)


# --------remove enrollment from course--------------
def remove_enrollment_from_course(student_id, course_id):
    try:

        with open("data/enrollments.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        print("no enrollments exist")

    updated_list = {}
    for enrollment in data:
        if (
            enrollment["student_id"] == student_id
            and enrollment["course_id"] == course_id
        ):
            continue

        updated_list.append(enrollment)

    with open("data/enrollments.json", "w") as file:
        json.dump(updated_list, file, indent=4)
