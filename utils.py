def _is_valid_grade(grade):
    try:
        grade_num = int(grade)
        return 0 <= grade_num <= 100
    except (ValueError, TypeError):
        return False


def _is_valid_studentID(id):
    if isinstance(id, int):
        if id >= 0:
            return True
    return False


def _is_valid_courseID(id):
    if isinstance(id, int):
        if id >= 0:
            return True
    return False


def _is_existing_student(data, id):
    for student in data["students"]:
        if student["id"] == id:
            return True

    return False


def _is_existing_courseID(data, id):
    for enrollment in data["courses"]:
        if enrollment["id"] == id:
            return True

    return False


def _is_valid_age(age):
    if isinstance(age, int):
        if age >= 1 and age <= 100:
            return True

    return False
