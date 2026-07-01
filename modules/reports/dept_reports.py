import numpy as np
import pandas as pd
import json


def __load_students():
    with open("data/students.json", "r") as file:
        data = json.load(file)

    return data


def students_in_each_dept():
    data = __load_students()

    df= pd.DataFrame(data["students"])
    count = df.groupby('department').size()

    print(count)
    return
