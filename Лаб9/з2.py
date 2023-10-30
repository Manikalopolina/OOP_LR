class PassengerPlane:# Объявляем класс 'Пассажирский самолет
    def __init__(self, name, year, capacity):# определяем конструктор класса, который принимает аргументы name, year, capacity
        self.name = name # присваиваем аргументу name значение self.name
        self.year = year # присваиваем аргументу  year значение self.year
        self.capacity = capacity # присваиваем аргументу capacity значение self.capacity

    def get_info(self):# создаём метод о выводе информации
        return f"Название: {self.name}\nГод выпуска: {self.year}\nВместимость: {self.capacity} пассажиров"


class CargoPlane:# Объявляем класс'Грузовой самолет'
    def __init__(self, name, year, load_capacity):
        self.name = name # присваиваем аргументу name значение self.name
        self.year = year # присваиваем аргументу  year значение self.year
        self.load_capacity = load_capacity # присваиваем аргументу load_capacity значение self.load_capacity

    def get_info(self):# создаём метод о выводе информации
        return f"Название: {self.name}\nГод выпуска: {self.year}\nГрузоподъемность: {self.load_capacity} тонн"

# создание экземпляров класса
airplane1 = PassengerPlane("Boeing 747", 2000, 400)
airplane2 = CargoPlane("Airbus A330", 2010, 50)
# вывод информации
print(airplane1.get_info())
print()
print(airplane2.get_info())
