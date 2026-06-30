import json


def __load_enrollments():
    with open("data/enrollments.json", "r") as file:
        data = json.load(file)

    return data


def students_in_each_course():
    data = __load_enrollments()
    courses = {}
    for enrollment in data["enrollments"]:
        for course_id in enrollment["course_id"]:
            courses[course_id] = courses.get(course_id, 0) + 1

    return courses