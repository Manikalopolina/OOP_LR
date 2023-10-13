

class Student:
    '''Класс, представляющий модель студента.
       Аргументы:
    - name (str): Фамилия и имя студента.
    - group_number (str): Номер группы.
    - academic_perfomance (list): Список из пяти элементов, представляющий успеваемость студента.
    - gpa_scores (float): Средний балл студента, автоматически вычисляемый как сумма оценок деленная на 5.'''
    def __init__(self, name, group_number, academic_perfomance):
        self.name = name
        self.group_number = group_number
        self.academic_perfomance = academic_perfomance
        self.gpa_scores = sum(self.academic_perfomance) / 5

    def print_info(self):
        ''' Метод для вывода информации о студенте.
            Аргументы:
            -Номер группы (str)
            -Успеваемость (list)
            -Средний бал (float)'''
        print(f'ФИ: {self.name}\n  Номер группы: {self.group_number}\n'
              f'  Успеваемость: {self.academic_perfomance}\n'
              f'  Средний балл: {self.gpa_scores}\n')
