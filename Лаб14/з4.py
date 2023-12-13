from tkinter import *
from math import cos

def tabulate_function():
    # Очищаем список перед табуляцией функции
    listbox.delete(0, END)

    # Получаем значение шага и диапазон параметра
    step = 0.01
    start = 0.01
    end = 0.9

    # Вычисляем количество итераций для табуляции
    iterations = int((end - start) / step) + 1

    # Выводим формулу функции
    label_function_formula.config(text="2.5 + cos(-x)", fg='darkred', bg='pink')

    # Выводим заголовок таблицы
    listbox.insert(END, "    x         |         y")

    # Табулируем функцию и добавляем результаты в список
    for i in range(iterations):
        x = start + i * step
        y = 2.5 + cos(-x)
        result = f"   {x:.2f}              {y:.2f}"
        listbox.insert(END, result)

# Создаём графический интерфейс
r = Tk()
r.title("Расчет функции")

# Создаём метку для отображения формулы
label_function_formula = Label(r, text="")
label_function_formula.pack()

# Создаём кнопку для табуляции функции
tabulate_button = Button(r, text="Расчет", fg='darkblue', bg='lightblue', command=tabulate_function)
tabulate_button.pack()

# Создаём список для отображения результатов
listbox = Listbox(r)
listbox.pack()

r.mainloop()