# Создаем класс Таксопарк
class TaxiPark:
    # Инициализируем поля класса
    def __init__(self, make, model, fuel_consumption, speed):
        self.make = make  # Марка автомобиля
        self.model = model  # Модель автомобиля
        self.fuel_consumption = fuel_consumption  # Расход топлива автомобиля
        self.speed = speed  # Скорость автомобиля
    # Создаем свойства для доступа к полям класса
    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, make):
        self._make = make

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, fuel_consumption):
        self._fuel_consumption = fuel_consumption

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed

    def __repr__(self):
        return f"{self.make} {self.model}"


# Создаем список объектов класса TaxiPark
taxi_park = [
    TaxiPark("Toyota", "Camry", 8, 200),
    TaxiPark("Honda", "Civic", 7.2, 180),
    TaxiPark("Ford", "Focus", 6.8, 190),
    TaxiPark("Chevrolet", "Cruze", 7, 175),
    TaxiPark("Volkswagen", "Passat", 6.5, 210)]
# Сортируем автомобили по расходу топлива
taxi_park.sort(key=lambda car: car.fuel_consumption)
# Выводим отсортированный список автомобилей
print("Список автомобилей в таксопарке:")
for car in taxi_park:
    print(f"{car.make} {car.model} - расход топлива: {car.fuel_consumption} л/100 км")
# Задаем диапазон параметров скорости
min_speed = 180
max_speed = 200
# Находим автомобиль, соответствующий заданному диапазону параметров скорости
matched_cars = [car for car in taxi_park if min_speed <= car.speed <= max_speed]
# Выводим найденные автомобили
print(f"\nАвтомобили со скоростью от {min_speed} км/ч до {max_speed} км/ч:")
for car in matched_cars:
    print(f"{car.make} {car.model} - скорость: {car.speed} км/ч")