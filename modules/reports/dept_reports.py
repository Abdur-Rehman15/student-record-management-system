import numpy as np
import pandas as pd
import json


def __load_students():
    with open("data/students.json", "r") as file:
        data = json.load(file)

    return data

import pandas as pd

def students_in_each_dept():
    data = __load_students()

    df = pd.DataFrame(data["students"])
    count = df.groupby('department').size()

    print(f"\n\033[34mDepartment\033[0m{' ' * 15}\033[34mStudents Count\033[0m")
    
    for dept, num in count.items():
        print(f"\033[36m{dept:<25}\033[0m \033[32m{num}\033[0m")
        
    return

