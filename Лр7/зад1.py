class Customer:
    def __init__(self, lastname, firstname, middlename, address, phone, creditcardnumber, bankaccountnumber):
        # Конструктор класса Customer, принимает аргументы lastname, firstname, middlename, address, phone, creditcardnumber и bankaccountnumber
        # для инициализации свойств объекта Customer.
        self.lastname = lastname
        self.firstname = firstname
        self.middlename = middlename
        self.address = address
        self.phone = phone
        self._creditcardnumber = creditcardnumber
        self._bankaccountnumber = bankaccountnumber

    @property
    def creditcardnumber(self):
        return self._creditcardnumber

    @creditcardnumber.setter
    def creditcardnumber(self, value):
        self._creditcardnumber = value

    @property
    def bankaccountnumber(self):
        return self._bankaccountnumber

    @bankaccountnumber.setter
    def bankaccountnumber(self, value):
        self._bankaccountnumber = value

customer = Customer("Маникало", "Полина", "Александровна", "Мосты", "+375259555898", "1234567890123456", "1234567890")
# Создаем объект customer  с передачей всех необходимых аргументов.

print(customer.creditcardnumber)
# Выводим значение свойства creditcardnumber
print(customer.bankaccountnumber)
# Выводим значение свойства bankaccountnumber
customer.creditcardnumber = "9876543210987654"
# Изменяем значение свойства creditcardnumber
customer.bankaccountnumber = "0987654321"
# Изменяем значение свойства bankaccountnumber
print(customer.creditcardnumber)
# Выводим измененное значение свойства creditcardnumber
print(customer.bankaccountnumber)
# Выводим измененное значение свойства bankaccountnumber