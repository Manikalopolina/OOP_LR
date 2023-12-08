# Импортирование модуля tkinter для создания графического интерфейса
from tkinter import *
# Импортирование виджета ttk из модуля tkinter для расширенной работы с графическим интерфейсом
from tkinter import ttk

# Создание окна с указанными размерами
window = Tk()
window.geometry("300x80")
value_var = IntVar() # Создание переменной, которая будет связана с полосой прогресса
# Создание полосы прогресса с указанными параметрами
pb = ttk.Progressbar(window, orient="horizontal", length=280, variable=value_var, mode='determinate')
pb.pack() # Отображение полосы прогресса


# Функция, которая запускает полосу прогресса с указанной скоростью
def start():
    pb.start(10)


# Функция, которая останавливает полосу прогресса
def stop():
    pb.stop()

start_btn=ttk.Button(text="Start", command=start) # Создание кнопки "Start" с указанной надписью и указанным
# действием при клике
start_btn.pack() # Отображение кнопки
stop_btn=ttk.Button(text="Stop", command=stop) # Создание кнопки "Stop"
# с указанной надписью и указанным действием при клике
stop_btn.pack() # Отображение кнопки

window.mainloop()