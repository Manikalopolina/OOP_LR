class Rectangle:# объявляем класс "Прямоугольник"
    def __init__(self, a, b): # определяем конструктор класса, который принимает два аргумента a и b
        self.a=a # присваиваем аргументу a значение self.a
        self.b=b # присваиваем аргументу b значение self.b
    def get_area(self):  # определяем метод класса get_area
        return self.a*self.b # возвращаем произведение self.a и self.b
class Square: # объявляем класс "Квадрат"
    def __init__(self, a):  # определяем конструктор класса, который принимает аргумент a
        self.a=a # присваиваем аргументу a значение self.a
    def get_area(self): # определяем метод класса get_area
        return self.a**2 # возвращаем квадрат self.a
class Circle: #  объявляем класс "Круг"
    def __init__(self, r): # определяем конструктор класса, принимает аргумент r
        self.r=r # присваиваем аргументу r значение self.r
    def get_area(self): # определяем метод класса get_area
        return 3.14*self.r**2  # возвращаем площадь круга с радиусом self.r
# создаем объекты классов
rect1=Rectangle(3, 4)
rect2=Rectangle(12, 3)
sql=Square(2)
circle=Circle(3)
figure=[rect1, rect2, sql, circle]  # создаем список объектов классов
for figure in figure: # для каждого объекта в списке
    print(figure.get_area())# выводим его площадь
