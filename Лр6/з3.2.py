import з3

def personswithhighereducation(persons):
    '''Функция, которая получает список объектов класса Person
    и возвращает список объектов с высшим образованием.
    Аргументы:
    - persons (list): Список объектов класса Person.
    Возвращает:
    - p_list: Список объектов с высшим образованием.'''
    p_list=[]
    for el in persons:
        if el.education=='Высшее':
            p_list.append(el)
    return p_list

persons=[з3.Person ('Маникало', 'Полина', 'Александровна', 'Мосты', 'Женский', 'Высшее', 2007),
         з3.Person ('Белуш', 'Дарья', 'Руслановна', 'Дятлово', 'Женский', 'среднее', 2006),
         з3.Person ('Макей', 'Арина', 'Александровна', 'Островец', 'Женский', 'среднее', 2007),
         з3.Person ('Капыш', 'Вероника', 'Александровна', 'Сморгонь', 'Женский', 'среднее', 2006),
         з3.Person ('Лужинская', 'Мария', 'Юрьевна', 'Воложина', 'Женский', 'среднее', 2007)]


high_education_list=personswithhighereducation(persons)
for person in high_education_list:
    person.print_info()
