class Volunteer:
    def __init__(self, name='', surname='', city=''):
        self.surname = surname
        self.name = name
        self.city = city


class Guest(Volunteer):
    def __init__(self, name, surname, city, status):
        super().__init__(name, surname, city)
        self.status = status

    def guest_list(self):
        return f'{self.name} {self.surname}, г.{self.city}, статус: {self.status}'


list_employees = [{'name': 'Олег', 'surname': 'Иванов', 'city': 'Москва', 'job': 'Слесарь', 'status': 'Координатор'},
                  {'name': 'Виктор', 'surname': 'Тяпкин', 'city': 'Вологда', 'job': 'Слесарь', 'status': 'Волонтер'},
                  {'name': 'Василий', 'surname': 'Пупкин', 'city': 'Москва', 'job': 'Переводчик', 'status': 'Наставник'},
                  {'name': 'Дмитрий', 'surname': 'Бурак', 'city': 'Минск', 'job': 'Программист',
                   'status': 'Наставник'},
                  {'name': 'Иван', 'surname': 'Иванов', 'city': 'Воронеж', 'job': 'Повар',
                   'status': 'Координатор'},
                  {'name': 'Татьяна', 'surname': 'Сидорова', 'city': 'Самара', 'job': 'Экономист',
                   'status': 'Координатор'}
                  ]

print('Список приглашённых: ')
print()
for list_e in list_employees:
    for e in list_e:
        if e == 'job' and list_e['job'] == 'Слесарь':
            guest = Guest(list_e['name'], list_e['surname'], list_e['city'], list_e['status'])
            print(guest.guest_list())
