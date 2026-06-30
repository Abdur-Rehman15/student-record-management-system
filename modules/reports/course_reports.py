import numpy as np
import pandas as pd
import json


def __load_enrollments():
    with open("data/enrollments.json", "r") as file:
        data = json.load(file)

    return data


def students_in_each_course():
    data = __load_enrollments()
    # abhi pta ni kesy hoga ye
