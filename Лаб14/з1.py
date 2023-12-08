# Импорт модулей tkinter и ttk из tkinter
from tkinter import *
from tkinter import ttk


# Определение функции getInfo
def getInfo():
    # Открытие файла 'output.txt' в режиме записи с кодировкой utf-8
    file = open('output.txt', 'w', encoding='utf-8')
    # Запись имени в файл с использованием метода format
    file.write('Имя: {}\n'.format(nameT.get()))
    # Запись фамилии в файл с использованием метода format
    file.write('Фамилия: {}\n'.format(lastNameT.get()))
    # Проверка значения переменной polvar и запись соответствующего значения в файл
    if polvar.get() == 'm':
        file.write('Пол: мужской\n')
    elif polvar.get() == 'w':
        file.write('Пол: женский\n')
    else:
        file.write('Пол не указан\n')
    # Запись любимых предметов в файл
    file.write('Любимые предметы:\n')
    if var1.get() == 1:
        file.write(' - математика\n')
    if var2.get() == 1:
        file.write(' - английский язык\n')
    if var3.get() == 1:
        file.write(' - информационные технологии\n')

# Создание главного окна tkinter
window = Tk()
# Задание заголовка окна
window.title('Регистрация')
# Создание надписей Label для отображения текста
name = Label(window, text='Имя', width=20, height=1, fg='blue', font='arial 18')
lastName = Label(window, text='Фамилия', width=20, height=1, fg='blue', font='arial 18')
pol = Label(window, text='Пол', width=20, height=1, fg='blue', font='arial 18')
likePr = Label(window, text='Любимые предметы', width=20, height=1, fg='blue', font='arial 18')
# Создание полей для ввода текста Entry
nameT = Entry(window, width=30, font='arial 14')
lastNameT = Entry(window, width=30, font='arial 14')
# Создание переменной для хранения выбранного значения переключателя Radiobutton
polvar = StringVar()
# Установка начального значения переменной polvar
polvar.set(' ')
# Создание переключателей для выбора пола
radio1 = Radiobutton(window, text='мужской', variable=polvar, value='m')
radio2 = Radiobutton(window, text='женский', variable=polvar, value='w')
# Создание переменных для хранения состояния флажков Checkbutton
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
# Создание флажков для выбора любимых предметов
check1 = Checkbutton(window, text='математика', variable=var1, onvalue=1, offvalue=0)
check2 = Checkbutton(window, text='английский язык', variable=var2, onvalue=1, offvalue=0)
check3 = Checkbutton(window, text='информационные технологии', variable=var3, onvalue=1, offvalue=0)
# Создание кнопки с заданными свойствами
btn = Button(window, text='Принять', width=25, height=5, fg='blue', font='arial 14', command=getInfo)
# Упаковка элементов виджетов в окне
name.pack()
nameT.pack()
lastName.pack()
lastNameT.pack()
pol.pack()
radio1.pack()
radio2.pack()
likePr.pack()
check1.pack()
check2.pack()
check3.pack()
btn.pack()
window.mainloop()