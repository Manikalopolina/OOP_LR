class Company:
    def __init__(self, name): # Определение конструктора класса Company, принимающего параметр name
        self.nname=name # Присвоение значению атрибута nname=name

    @property
    def name(self): # Определение геттера для свойства name
        return self.nname  # Возврат значения атрибута nname

    @name.setter
    def name(self, name): # Определение сеттера для свойства name
        self.nname=name # Присвоение нового значения атрибуту nname


class Tariff:
    def __init__(self, name, subscribers): # Определение конструктора класса Tariff, принимающего параметры name
        # и subscribers
        self.nname = name # Присвоение значению атрибута nname=name
        self.ssubscribers=subscribers # Присвоение значению атрибута ssubscribers=subscribers


    @property
    def name(self): # Определение геттера для свойства name
        return self.nname # Возврат значения атрибута nname

    @name.setter
    def name(self, name): # Определение сеттера для свойства name
        self.nname=name # Присвоение нового значения атрибуту nname

    @property
    def subscribers(self): # Определение геттера для свойства subscribers
        return self.ssubscribers # Возврат значения атрибута ssubscribers

    @subscribers.setter
    def subscribers(self, subscribers): # Определение сеттера для свойства subscribers
        self.ssubscribers=subscribers # Присвоение нового значения атрибуту ssubscribers

    def calculate_call_cost(self, seconds): # Определение метода calculate_call_cost класса Tariff
      pass


class PerSecondTariff(Tariff):
    def __init__(self, name, subscribers, call_rate): # Определение конструктора класса PerSecondTariff, принимающего
        # параметры name, subscribers и call_rate
        super().__init__(name, subscribers) # Вызов конструктора родительского класса
        self.ccall_rate=call_rate # Присвоение значению атрибута ccall_rate экземпляра класса


    @property
    def call_rate(self): # Определение геттера для свойства call_rate
        return self.ccall_rate # Возврат значения атрибута ccall_rate

    @call_rate.setter
    def call_rate(self, call_rate): # Определение сеттера для свойства call_rate
        self.ccall_rate=call_rate # Присвоение нового значения атрибуту ccall_rate

    def calculate_call_cost(self, seconds): # Определение метода calculate_call_cost класса PerSecondTariff
        try:
            if seconds<0: # Проверка условия: количество секунд отрицательное
                raise ValueError('Количество секунд не может быть отрицательным') # Вызов исключения ValueError
            cost=seconds*self.ccall_rate  # Вычисление стоимости разговора
            return cost # Возврат стоимости разговора
        except ValueError : # Обработка исключения ValueError
            print("Error:Количество секунд не может быть отрицательным") # Обработка исключения ValueError


class PerMinuteTariff(Tariff):
    def __init__(self, name, subscribers, call_rate): # Определение конструктора класса PerMinuteTariff, принимающего
        # параметры name, subscribers и call_rate
        super().__init__(name, subscribers) # Вызов конструктора родительского класса
        self.ccall_rate=call_rate # Присвоение значению атрибута ccall_rate экземпляра класса

    @property
    def call_rate(self): # Определение геттера для свойства call_rate
        return self.ccall_rate # Возврат значения атрибута ccall_rate

    @call_rate.setter
    def call_rate(self, call_rate): # Определение сеттера для свойства call_rate
        self.ccall_rate=call_rate # Присвоение нового значения атрибуту ccall_rate

    def calculate_call_cost(self, seconds): # Определение метода calculate_call_cost класса PerMinuteTariff
        try:
            if seconds<0: # Проверка условия: количество секунд отрицательное
                raise ValueError('Количество секунд не может быть отрицательным')# Вызов исключения ValueError
            minutes=seconds//60  # Вычисление количества минут
            if seconds%60>0:
                minutes+=1
            cost=minutes * self.ccall_rate # Вычисление стоимости разговора
            return cost  # Возврат стоимости разговора
        except ValueError: # Обработка исключения ValueError
            print('Error:Количество секунд не может быть отрицательным') # Вывод сообщения об ошибке

class Subscriber:
    def __init__(self, full_name, phone_number, balance): # Определение конструктора класса Subscriber, принимающего
        # параметры full_name, phone_number и balance
        self.ffull_name=full_name # Присвоение значению атрибута ffull_name экземпляра класса
        self.pphone_number=phone_number # Присвоение значению атрибута pphone_number экземпляра класса
        self.bbalance=balance  # Присвоение значению атрибута pphone_number экземпляра класса

    @property
    def full_name(self): # Определение геттера для свойства full_name
        return self.ffull_name # Возврат значения атрибута ffull_name

    @full_name.setter
    def full_name(self,full_name): # Определение сеттера для свойства full_name
        self.ffull_name=full_name # Присвоение нового значения атрибуту ffull_name

    @property
    def phone_number(self): # Присвоение нового значения атрибуту ffull_name
        return self.pphone_number # Возврат значения атрибута pphone_number

    @phone_number.setter
    def phone_number(self,phone_number): # Определение сеттера для свойства phone_number
        self.pphone_number=phone_number # Присвоение нового значения атрибуту pphone_number

    @property
    def balance(self): # Определение геттера для свойства balance
        return self.bbalance # Возврат значения атрибута bbalance

    @balance.setter
    def balance(self,balance): # Определение сеттера для свойства balance
        self.bbalance=balance # Присвоение нового значения атрибуту bbalance

# Пример использования
company=Company("Моя компания") # Создание компании
per_second_tariff=PerSecondTariff("Посекундный тариф", 2000, 0.01) # Создание тарифа посекундной оплаты
company.tariff=per_second_tariff # Установка тарифа компании
subscriber=Subscriber("Иван Иванов", "123456789", 300) # Создание абонента
cost=per_second_tariff.calculate_call_cost(600) # Рассчет стоимости разговора
print(f"Стоимость разговора: {cost}")
cost=per_second_tariff.calculate_call_cost(-100) # отрицательное количество секунд
