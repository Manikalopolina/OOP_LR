class Transport: # Создание базового класса "Transport"
    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f'Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч'


class Car(Transport): # Создание класса "Car", наследующего от "Transport"

    def __init__(self, brand, max_speed, mileage, gasoline_residue):
        super().__init__(brand,max_speed,kind='Car') # Вызов инициализатора родительского класса
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue

    @property
    def gasoline(self): # Геттер для получения остатка бензина
        return f'Осталось бензина на {self.__gasoline_residue} км'

    @gasoline.setter
    def gasoline(self, value): # Сеттер для увеличения объема бензина
        if isinstance(value,int): # Проверка, является ли значение целым числом
            self.__gasoline_residue += value # Увеличение объема бензина
            print(f'Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л')
        else:
            print('Ошибка заправки автомобиля')

class Boat(Transport): # Создание  класса "Boat", наследующего от "Transport"


    def __init__(self, brand, max_speed, owners_name):
        super().__init__(brand, max_speed, kind='Boat') # Вызов инициализатора родительского класса
        self.owners_name = owners_name

    def __str__(self):
        return f'Этой лодкой марки {self.brand} владеет {self.owners_name}'


class Plane(Transport): # Создание  класса "Plane", наследующего от "Transport"

    def __init__(self, brand, max_speed, capacity):
        super().__init__(brand, max_speed, kind='Plane') # Вызов инициализатора родительского класса
        self.capacity = capacity

    def __str__(self):
        return f'Самолет марки {self.brand} вмещает в себя {self.capacity} людей'

car = Car('Audi', 250, 10000, 50)
boat = Boat('Yamaha', 80, 'John')
plane = Plane('Boeing', 900, 300)
print(car)
print(boat)
print(plane)