class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, age = {self.age}, gender = {self.gender}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"

class Group:

    def __init__(self, number):
        self.number = number
        # self.group = set()
        self.group = []

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError(f"Cannot add {student.first_name} {student.last_name}, because group is full")
        if student not in self.group:
            self.group.append(student)

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

class GroupLimitError(Exception):
    def __init__(self, text="The limit of 10 students has been exceeded! Please, keep the number of students up to the specified limit"):
        super().__init__(text)


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!

try:
    for person in range(1, 12):
        student = Student("Other", 22, "Tutti", "Frutti", "AN222")
        gr.add_student(student)
except GroupLimitError as err:
    print(err)























