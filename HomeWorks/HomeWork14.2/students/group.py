from .student import Student
from .group_limit import GroupLimitError

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()
        # self.group = []

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError(f"Cannot add {student.first_name} {student.last_name}, because group is full")
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        self.group.remove(student) if student else None

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None
        # return next((student for student in self.group if student.last_name == last_name), None)

    def __str__(self):
        all_students = "\n".join("  " + str(student) for student in self.group)
        return f'Number:{self.number}\n{all_students} '


