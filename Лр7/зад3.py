import random
class Flower:
    def __init__(self, stem_length, freshness):
        self.__stem_length=stem_length
        self.__freshness=freshness
    @property # декоратор, который позволяет использовать методы как атрибуты только для чтения.
    def stem_length(self):
        return self.__stem_length
    @stem_length.setter # декоратор, который позволяет использовать метод stem_length для установки значения атрибута __stem_length.
    def stem_length(self, value):
        if not isinstance(value, int): # проверка, является ли значение value целым числом.
            print('Длина стебля должна быть числом')# вывод сообщения, если value не является целым числом.
        elif value<5: # проверка, меньше ли значение value 5.
            print('Длина стебля должна быть минимум 5') # вывод сообщения, если значение value меньше 5.
        elif value>20: # проверка, больше ли значение value 20.
            print('Длина стебля должна быть максимум 20') # вывод сообщения, если значение value больше 20.
        else: # в другом случае
            self.__stem_length=value #  установка значения атрибута __stem_length равным value.
    @property
    def freshness(self):
        return self.__freshness
    @freshness.setter
    def freshness(self, value):
        if not isinstance(value, int):
            print('Уровень свежести должен быть числом')
        elif value<1:
            print('Уровень свежести должен быть минимум 1')
        elif value>10:
            print('Уровень свежести должен быть максимум 10')
        else:
            self.__freshness=value
# Создание списка объектов класса Flower, для которых значение атрибутов-случайные числа.
f=[]
for i in range(5):
    f.append(Flower(int(random.uniform(5, 20)), int(random.uniform(1, 10))))
    print(f'Цветок {i+1}: длина стебля {f[i].stem_length}, уровень свежести {f[i].freshness}')
# Сортировка списка объектов класса по атрибуту freshness
result=sorted(f, key=lambda x: x.freshness)
# Вывод элементов отсортированного списка
print('\nОтсортированный букет:')
for i in range(5):
    print(f'Цветок {i+1}-уровень свежести {result[i].freshness}')
# задание диапазона длины стебля
start=int(input('Введите начальное значение диапазона: '))
end=int(input('Введите конечное значение диапазона: '))
# Вывод элементов списка заданного диапазона
for i in range(5):
    if start<=f[i].stem_length<=end:
        print(f'Цветок {i+1}-длина стебля {f[i].stem_length}')