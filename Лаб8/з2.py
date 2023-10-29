class Vector:
    def __init__(self,*args): # Конструктор получает произвольное количество аргументов
        self.values=[] # Создаём пустой список
        for arg in args: # Начало цикла for, перебираем каждый аргумент
            if isinstance(arg,int): # Проверяем, является ли аргумент целым числом
                self.values.append(arg) # Добавляем аргумент в список значений
            self.values.sort() # Используем функцию sort для сортировки всех значений

    def __str__(self): # Вызываем метод __str__ для преобразования объекта в строку
        if len(self.values)==0: # Проверяем, пустой ли список значение
            return 'пусть вектор' # Если условие истино, то возвращаем строку
        return f'вектор{tuple(self.values)}' # Возвращаем строку и кортеж

    def __add__(self, other): # Вызываем метод __add__, который отвечает за сложение объектов
        new_v=[] # Создаём пустой список
        if isinstance(other, Vector): # Проверяем, является ли other объектом класса Vector
            if len(self.values)==len(other.values): # Проверяем, равной ли длины векторы
                for i in range(len(self.values)): # Начало цикла for
                    new_v.append(self.values[i] + other.values[i]) # Добавляем сумму значений в новый список
                return Vector(*[i for i in new_v]) # Создаём новый объект с новым списком значений
            else: # В другом случае
                print('сложение векторов разной длины недопустимо.') # Выводим на экран сообщение об ошибке
        if isinstance(other, int): # Проверяем, является ли other целым числом
            for i in range(len(self.values)): # Начало цикла for
                new_v.append(self.values[i]+other) # Добавляем сумму каждого значения с other в новый список
            return Vector(*[i for i in new_v]) # Создаём новый объект с новым списком значений
        if not isinstance(other, (Vector, int)): # Проверяем, не является ли other объктом класса Vector и целым числом
                print(f'Вектор нельзя сложить с {other}') # Выводим на экран сообщение об ошибке

    def __mul__(self, other): # Вызываем метод __mul__, который отвечает за умножение
        new_v=[] # Создаём новый пустой список
        if isinstance(other, Vector): # Проверяем, является ли other объектом класса Vector
                if len(self.values)==len(other.values): # Проверяем, равны ли длины векторов
                    for i in range(len(self.values)): # Начало цикла for, перебираем каждое число
                        new_v.append(self.values[i] * other.values[i]) # Добавляем произведение значений в новый список
                    return Vector(*[i for i in new_v]) # Создаём новый объект с новым списком значений
                else: # Иначе
                    print('сложение векторов разной длины недопустимо.') # Выводи на экран сообщение об ошибке
        if isinstance(other, int): # Проверяем, является ли other целым числом
            for i in range(len(self.values)): # Начало цикла for, перебираем каждое число
                new_v.append(self.values[i]*other) # Добавляем произведение чисел
            return Vector(*[i for i in new_v]) # Возвращаем значение
        if not isinstance(other, (Vector, int)): # Проверяем, не является ли other объектом класса Vector и целым числом
                print(f'Вектор нельзя сложить с {other}') # Если условие истино, выводи на экран сообщение

v1=Vector(1,2,3) # Создаем объект v1 со значениями
print(v1) # Выводим на экран результат
v2=Vector(4,7,1,12) # Создаем объект v1 со значениями
print(v2) # Выводим на экран результат
print(v1+v2) # Выводим на экран результат
v3=Vector(7,11,3,18) # Создаем объект v1 со значениями
print(v2+v3) # Выводим на экран результат
v4=Vector(4,6,8)# Создаем объект v1 со значениями
v5=Vector(5,3,2) # Создаем объект v1 со значениями
print(v4*v5) # Выводим на экран результат