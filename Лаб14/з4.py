from tkinter import *
from tkinter import ttk


# Создаём функцию для табулирования функции
def tabulate_function():
    # Очищаем список перед табуляцией функции
    listbox.delete(0, END)

    # Получаем значение шага и диапазон параметра
    st = 0.01
    beg = 0.01
    end = 0.9

    # Вычисляем количество итераций для табуляции
    it = int((end - beg) / st) + 1

    # Выводим формулу функции
    label_function_formula.config(text="y = 2 * x + 0.33", fg='darkred', bg='pink')

    # Выводим заголовок таблицы
    listbox.insert(END, "    x         |         y")

    # Табулируем функцию и добавляем результаты в список
    for i in range(it):
        x = beg + i * st
        y = 2 * x + 0.33
        result = f"   {x:.2f}              {y:.2f}"
        listbox.insert(END, result)

    # Создаём графический интерфейс


root = Tk()
root.title("Расчет функции")
# Создаём метку для отображения формулы
label_function_formula = Label(root, text="")
label_function_formula.pack()
# Создаём кнопку для табуляции функции
tabulate_button = Button(root, text="Расчет", fg='darkblue', bg='lightblue', command=tabulate_function)
tabulate_button.pack()
# Создаём список для отображения результатов
listbox = Listbox(root)
listbox.pack()
root.mainloop()