# Импортируем все классы и функции из модуля tkinter для создания графического интерфейса, а также
# функции sqrt, exp и log из модуля math для математических вычислений.
from tkinter import *
from math import sqrt, exp, log


def calculate_formula(): # Объявляем функцию calculate_formula, которая будет вызываться при нажатии на кнопку
    # "Вычислить".
    x = float(entry.get()) # Извлекаем значение из виджета entry и преобразуем его в число с
    # помощью функции float().
    result = (sqrt(pow(exp(1/3 - x), 5))) / sqrt(x**2 + x**4 + abs(log(abs(x - 3.4)))) # Вычисляем значение выражения
    # по формуле.
    result_label.config(text="Выражение = " + str(result)) # Устанавливаем текст для result_label
# Создаем главное окно приложения с помощью класса Tk(). Задаем заголовок окна  и размеры пикселей.
window = Tk()
window.title("Формула")
window.geometry('500x100')
# Создаем label1 и добавляем его на главное окно.
# Устанавливаем текст и цвет текста. Размещаем метку в 2-ом столбце и 0-й строке .
label1 = Label(window, text="Подсчет по формуле", fg='blue')
label1.grid(column=2, row=0)
# Создаем label  и добавляем его на главное окно. Устанавливаем текст "x = ".
# Размещаем метку в 1-ом столбце и 1-й строке
label = Label(window, text="x = ")
label.grid(column=1, row=1)
# Создаем  entry  и добавляем его на главное окно. Размещаем поле в 2-ом столбце и 1-й строке.
entry = Entry(window)
entry.grid(column=2, row=1)
# Создаем  calculate_button  и добавляем его на главное окно.
# Устанавливаем текст  и связываем с кнопкой функцию calculate_formula.
# Размещаем кнопку в 2-ом столбце и 2-й строке.
calculate_button = Button(window, text="Вычислить", command=calculate_formula)
calculate_button.grid(column=2, row=2)
# Создаем result_label  и добавляем его на главное окно.
# Устанавливаем текст. Размещаем метку в 1-ом столбце и 3-й строке.
result_label = Label(window, text="Выражение = ")
result_label.grid(column=1, row=3)

window.mainloop()