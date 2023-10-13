

class Person:
    ''' Класс, представляющий модель персоны.
    Аргументы:
    - last_name (str): Фамилия.
    - first_name (str): Имя.
    - middle_name (str): Отчество.
    - address (str): Адрес.
    - gender (str): Пол.
    - education (str): Образование.
    - birth_year (int): Год рождения.'''
    def __init__(self, last_name, first_name, middle_name, address, gender, education, birth_year):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.address = address
        self.gender = gender
        self.education = education
        self.birth_year = birth_year

    def print_info(self):
        '''Метод для вывода информации о персоне.'''
        print(f'ФИО: {self.last_name}{self.first_name}{self.middle_name}')
        print(f'Адрес: {self.address}')
        print(f'Пол:{self.gender}')
        print(f'Образование:{self.education}')
        print(f'Год рождения:{self.birth_year}')
