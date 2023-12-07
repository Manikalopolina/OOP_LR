from tkinter import * # Импорт модуля tkinter для создания графического пользовательского интерфейса
# Объявляем функцию clicked(). Она будет вызываться при нажатии на кнопку.
# Внутри функции мы изменяем текст lab1, устанавливаем шрифт и цвет текста на красный.
def clicked():
    lab1.configure(text='Первые  и не последние!', font=('Impact', 18), fg='blue')
# Объявляем функцию close_window(). Она будет вызываться при нажатии на кнопку "Закрыть".
# Внутри функции мы вызываем метод destroy() для закрытия окна.
def clise_window():
    window.destroy()


window=Tk() # Создаем  Tk(), который представляет окно приложения.
# Устанавливаем заголовок окна на "Проект 2" и размеры окна 500x200 пикселей.
window.title('Проект 2')
window.geometry('500x200')
lab=Label(window, text='Первые успехи!', font=('Impact', 15), fg='pink')
lab.grid(column=1, row=0)
# Создаем объект Label, который отображает текст в окне window.
lab=Label(window, text='')
lab.grid(column=1, row=0)
# Создаем второй объект Label, который будет использоваться для отображения измененного текста.
lab1=Label(window, text='', font=('Arial',14))
lab1.grid(column=1, row=0)
# Создаем кнопку с надписью "Приветствие".
# Устанавливаем ей функцию clicked() в качестве обработчика событий при нажатии кнопки.
btn=Button(window, text='Приветствие', font=('Arial',15), command=clicked)
btn.grid(column=0, row=1)
# Создаем вторую кнопку с надписью "Закрыть".
# Устанавливаем ей функцию close_window() в качестве обработчика событий при нажатии кнопки.
btn1=Button(window, text='Закрыть', font=('Arial',14), command=clise_window)
btn1.grid(column=2, row=1)
window.mainloop()

