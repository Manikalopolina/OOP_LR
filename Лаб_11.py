class Car: # Создаем класс Car
    def __init__(self, brand, model, color): # Определяем конструктор класса с параметрами brand, model, color
        self.brand=brand  # Присваиваем значение параметра brand атрибуту brand объекта класса
        self.model=model # Присваиваем значение параметра model атрибуту model объекта класса
        self.color=color # Присваиваем значение параметра color атрибуту color объекта класса

    def __str__(self): # Определяем метод str для вывода информации об объекте класса
        return f"Brand: {self.brand}\nModel: {self.model}\nColor: {self.color}"


class PassengerTransport(Car):  # Создаем класс PassengerTransport, который наследуется от класса Car
    def __init__(self, brand, model, color, number_of_seats): # Определяем конструктор класса с параметрами brand, model, color, numberofseats
        super().__init__(brand, model, color) # Вызываем конструктор родительского класса с параметрами brand, model, color
        self.number_of_seats=number_of_seats # Присваиваем значение параметра numberofseats атрибуту numberofseats объекта класса

    def __str__(self): # Определяем метод str для вывода информации об объекте класса
        return f"Brand: {self.brand}\nModel: {self.model}\nColor: {self.color}\nNumber of seats: {self.number_of_seats}"


class Bus(PassengerTransport): # Создаем класс Bus, который наследуется от класса PassengerTransport
    def __init__(self, brand, model, color, number_of_seats, numberoffloors): # Определяем конструктор класса с
        # параметрами brand, model, color, numberofseats, numberoffloors
        super().__init__(brand, model, color, number_of_seats) # Определяем конструктор класса с параметрами brand,
        # model, color, numberofseats, numberoffloors
        self.numberoffloors = numberoffloors# Присваиваем значение параметра numberoffloors атрибуту numberoffloors объекта класса


    def __str__(self):# Определяем метод str для вывода информации об объекте класса
        return f"Brand: {self.brand}\nModel: {self.model}\nColor: {self.color}\nNumber of seats: {self.number_of_seats}\nNumber of floors: {self.numberoffloors}"


# Пример использования классов:
car1 = Car("Toyota", "Camry", "red")
print(car1)

print("----------------")

transport1 = PassengerTransport("Hyundai", "Elantra", "blue", 5)
print(transport1)

print("----------------")

bus1 = Bus("Volvo", "B12", "white", 60, 2)
print(bus1)
