from dataclasses import dataclass


@dataclass
class Student:
    name: str
    id: int
    email_address: str
    age: int
    department: str

    def add_student(self, name: str, id: int, email_address: str, age: int, department: str):
        pass

    def update_student(self, name: str, id: int, email_address: str, age: int, department: str):
        pass

    def get_all_students(self):
        pass

    def search_student_by_ID(self, id: int):
        pass

    def delete_student(self, id: int):
        pass
