from dataclasses import dataclass


@dataclass
class Course:
    name: str
    id: int
    credit_hrs: int

    def add_course(self, name: str, id: int, credit_hrs: int):
        pass

    def delete_course(self, id: int):
        pass

    def view_all_courses(self):
        pass
