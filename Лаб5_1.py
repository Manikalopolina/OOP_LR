class C:# Создание класса А
    def __init__(self,a ,b=5):#Создаем конструктор класса C с аргументами a и b
        self.a=a#Присваиваем аргумент a атрибуту a объекта класса C
        self.b=b#Присваиваем аргумент b атрибуту b объекта класса C
    def c(self):#Создаем метод c без аргументов
        return self.a + self.b#Возвращает сумму атрибутов a и b
    def d(self):#Создаем метод d без аргументов
        return self.a-self.b#Возвращает разность атрибутов a и b

a1=C(5)#Создаем объект класса C с аргументом 5
print(f'{a1.a} + {a1.b} =', a1.c())#Выводим строку с результатом сложения атрибутов a и b объекта a1
a2=C(4,6)#Создаем объект класса C с аргументами 4 и 6
print(f'{a2.a} - {a2.b} =',a2.d())#Выводим строку с результатом разности атрибутов a и b объекта a2
