import з2
import random

def byGPA_key(person):
   ''' Функция для возвращения значения атрибута `gpa_scores` объекта класса Student.
    Используется в качестве ключа для сортировки списка студентов.
    Аргументы:
    - person (Student): Объект класса Student.
    Возвращает:
    - float: Значение среднего балла студента.'''
   return person.gpa_scores

students = [
    з2.Student(
        input('Введите фамилию и имя студента: '),
        input('Введите номер группы: '),
        [random.randint(1, 10) for i_grade in range(5)]
    )
    for i_student in range(10)
]

students_sort = sorted(students, key = byGPA_key)
for student in students_sort:
    student.print_info()
