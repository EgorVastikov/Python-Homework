students = {
    1: {'name': 'Bob', 'surname': 'Vazovski', 'age': 23, 'interests': ['biology', 'swimming']},
    2: {'name': 'Rob', 'surname': 'Stepanov', 'age': 24, 'interests': ['math', 'computer games', 'running']},
    3: {'name': 'Alexander', 'surname': 'Krug', 'age': 22, 'interests': ['languages', 'health food']}
}

def interests(students_dict):
    all_interests = set()
    total_surname_length = 0

    for student_details in students_dict.values():
        all_interests.update(student_details['interests'])
        total_surname_length += len(student_details['surname'])

    return all_interests, total_surname_length

student_age_pairs = [(student_id, details['age']) for student_id, details in students.items()]
interests, total_surname_length = interests(students)

print(f"Список пар «ID студента — возраст»: {student_age_pairs}")
print(f"Полный список интересов всех студентов: {interests}")
print(f"Общая длина всех фамилий студентов: {total_surname_length}")