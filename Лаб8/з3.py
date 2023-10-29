class Quadrilateral: # Создем класс Четырехугольник
    def __init__(self, width, height=0): # Задаем параметры с помощью конструктора
        self.width=width # Присваиваем переменную
        self.height=height # Присваиваем переменную

    def __str__(self): # Метод __str__ возвращает строку
        if self.width==self.height: # Проверяем, равны ли ширина и высота
            return f"Куб размером {self.width}х{self.height}" # Если условие истино, то возвращаем сообщение
        else: # В другом случае
            return f"Прямоугольник размером {self.width}х{self.height}" # Возвращаем сообщение

    def __bool__(self): # Метод __bool__ определяет логическое значение объекта
        return self.width==self.height # Возвращает правду, если ширина и высота равны

square=Quadrilateral(5, 5) # Создаем квадрат размером 5 на 5
print(square) # Выводим квадрат
print(bool(square)) # Если это квадрат, выведется True
rectangle=Quadrilateral(4, 6) # Создаем прямоугольник размером 4 на 6
print(rectangle) # Выводим прямоугольник
print(bool(rectangle)) # Если это квадрат, выводим True