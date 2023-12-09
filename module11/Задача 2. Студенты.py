class Student:
    def __init__(self, full_name, group_number, grades):
        self.full_name = full_name
        self.group_number = group_number
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.full_name}, Группа: {self.group_number}, Средний балл: {self.average_grade():.2f}"


students = [
    Student("Иванов Иван Иванович", "101", [4, 3, 5, 4, 5]),
    Student("Петров Петр Петрович", "102", [5, 4, 4, 5, 3]),
    Student("Сидоров Сидор Сидорович", "101", [3, 2, 3, 4, 2]),
    Student("Кузнецов Иван Олегович", "103", [4, 4, 4, 4, 4]),
    Student("Захарова Екатерина Андреевна", "102", [5, 5, 5, 5, 5]),
    Student("Морозов Иван Иванович", "104", [2, 3, 2, 3, 2]),
    Student("Васильев Дмитрий Алексеевич", "101", [3, 4, 3, 3, 4]),
    Student("Смирнов Сергей Сергеевич", "103", [4, 5, 4, 4, 5]),
    Student("Козлов Иван Андреевич", "102", [3, 3, 3, 3, 3]),
    Student("Зверев Зверь Зверевич", "104", [5, 4, 4, 4, 4])
]

students_sorted = sorted(students, key=lambda student: student.average_grade())
iter_student = iter(students_sorted)

for student in iter_student:
    print(student)