import json

# ===========error handling krni he course ids wgera ki abhi=========


# ----------new enrollment in course------------
def enroll_student_in_course(student_id, course_id):
    new_enrollment = {"student_id": student_id, "course_id": course_id}

    try:

        with open("data/enrollments.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        data = {"enrollments": []}

    for enrollment in data["enrollments"]:
        if enrollment["student_id"] == student_id:
            if course_id in enrollment["course_id"]:
                return "Student already enrolled in this course"
            
    data.append(new_enrollment)

    with open("data/enrollments.json", "w") as file:
        json.dump(data, file, indent=4)
      
    return "student enrolled successfully in the course"


# ----------view enrolled courses------------
def view_enrolled_courses(student_id):
    try:

        with open("data/enrollments.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        return "no enrollments exist"

    for enrollment in data["enrollments"]:
        if enrollment["student_id"] == student_id:
            return enrollment

    return "no enrollments found for this student"

# --------remove enrollment from course--------------
def remove_enrollment_from_course(student_id, course_id):
    try:

        with open("data/enrollments.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        return "no enrollments exist"

    updated_list = {"enrollments":[]}
    for enrollment in data["enrollments"]:
        if enrollment["student_id"] == student_id:
            new_list=[]
            for id in enrollment["course_id"]:
                if id!=course_id:
                    new_list.append(id)
            enrollment["course_id"] = new_list

        updated_list["enrollments"].append(enrollment)

    with open("data/enrollments.json", "w") as file:
        json.dump(updated_list, file, indent=4)
    
    return "enrollment removed successfully"
