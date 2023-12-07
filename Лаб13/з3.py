from tkinter import * # импортируем  все функции и классы из библиотеки tkinter
from random import randint # импортируем функцию randint из модуля random

# определяем функцию roll_dice, которая генерирует случайное число от 1 до 6 и выводит его на экран.
def roll_dice():
    label.configure(text=str(randint(1, 6)))

# определяем функцию close_window, которая закрывает окно.
def close_window():
    window.destroy()


window = Tk() # создаём главное окно приложения.
window.title("Брось кубик") # устанавливаем заголовок окна.
window.geometry('200x100') # устанавливаем размеры окна.

label = Label(window, text="Брось кубик", font=("Arial", 14), fg='orange') # создаём метку с текстом “Брось кубик”
# и устанавливаем шрифт и цвет текста.
label.pack() # добавляем метку в окно по середине

button = Button(window, text="Бросить кубик", font=("Arial", 14), command=roll_dice) # создаем метку с текстом
# “Брось кубик” и устанавливаем шрифт и цвет текста.
button.pack() # добавляем метку в окно по середине

window.mainloop()
