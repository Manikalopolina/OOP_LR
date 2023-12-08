from tkinter import *

window = Tk() # Создаем объект главного окна

window.geometry("250x200") # Устанавливаем размеры окна
list1 = Listbox(window, height=5, width=15, fg='purple', selectmode=EXTENDED) # Создаем объект Listbox для списка с возможностью
# выбора нескольких элементов
list2 = Listbox(window, height=5, width=15, fg='pink', selectmode=SINGLE) # Создаем второй объект Listbox для списка с возможностью
# выбора одного элемента
lst1 = ['Минск', 'Молодечно', 'Борисов', 'Жодино', 'Воложин','Дятлово'] # Создаем список элементов для первого Listbox
lst2 = ['Гродно', 'Ивье', 'Новогрудок', 'Ошмяны', 'Островец','Мосты'] # Создаем список элементов для второго Listbox

# Добавляем элементы из первого списка в первый Listbox
for i in lst1:
    list1.insert(END, i)

# Добавляем элементы из второго списка во второй Listbox
for i in lst2:
    list2.insert(END, i)
list1.pack() # Размещаем первый Listbox в окне
list2.pack() # Размещаем второй Listbox в окне

window.mainloop()
