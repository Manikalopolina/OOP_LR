class Student:
    def __init__(self,ФИ,Номер_группы,Успеваемость):
        self.ФИ=ФИ
        self.Номер_группы=Номер_группы
        self.Успеваемость=Успеваемость
    def print_info(self):
        print(f'ФИ:{self.ФИ},Номер_группы:{self.Номер_группы},Успеваемость:{self.Успеваемость}')
students=[]
for i in range(10):
    ФИ=input('Введите ФИ студента:')
    Номер_группы=input('Введите Номер группы студента:')
    Успеваемость=input('Введите успеваемость студента:')
    students.append(Student(ФИ,Номер_группы,Успеваемость))

for i in range(10):
    students[i].print_info()




