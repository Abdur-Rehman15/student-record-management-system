import numpy as np
import pandas as pd
import json


def __load_grades():
    with open("data/grades.json", "r") as file:
        data = json.load(file)

    return data


def top_performing_student():
    data = __load_grades()
    topper = "None"
    highest = 0
    for grades in data["grades"]:
        scores = [int(v) for v in grades["grades"].values()]
        avg = sum(scores) / len(scores)
        if avg > highest:
            topper = grades["student_id"]
            highest = avg

    print(f"Topper student has ID: {topper}")
    return


def avg_student_grade():
    data = __load_grades()
    all_averages = {}

    for entry in data["grades"]:
        student_id = entry["student_id"]
        scores = [int(v) for v in entry["grades"].values()]

        if scores:
            avg = sum(scores) / len(scores)
            all_averages[f"Student ID {student_id}"] = (
                f"avg grade of student is {avg}"
            )

    print(all_averages)
    return


def pass_fail_students_count():
    data = __load_grades()
    pass_count = 0
    fail_count = 0

    for entry in data["grades"]:
        scores = [int(v) for v in entry["grades"].values()]
        
        if scores:
            avg = sum(scores) / len(scores)
            if avg < 50:
                fail_count += 1
            else:
                pass_count += 1

    print("Passed:", pass_count, "Failed:", fail_count)
    return
