# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом
# премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров.
class Worker:
    salary_dict = {
        'программист': {"оклад": 60000, "премия": 10000},
        'директор': {"оклад": 100000, "премия": 30000},
        'секретарь': {"оклад": 40000, "премия": 5000},
    }

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = Worker.salary_dict[position]


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(self._income)


man_1 = Position('Иван', 'Иванов', 'программист')
man_2 = Position('Петр', 'Петров', 'директор')
man_3 = Position('Светлана', 'Сидорова', 'секретарь')
man_1.get_full_name()
man_1.get_total_income()
man_2.get_full_name()
man_2.get_total_income()
man_3.get_full_name()
man_3.get_total_income()
