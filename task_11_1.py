# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
# года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
import re


class Date:

    def __init__(self, inp_date):
        date = inp_date
        Date.valid_date(Date.convert_to_number(date))

    @classmethod
    def convert_to_number(cls, class_date):
        match = re.search(r'(\d{2})-(\d{2})-(\d{4})', class_date)
        cls.day = int(match.group(1))
        cls.month = int(match.group(2))
        cls.year = int(match.group(3))
        return cls.day, cls.month, cls.year

    @staticmethod
    def valid_date(*args):
        if 1 <= args[0][0] <= 31 and 1 <= args[0][1] <= 12 and 1990 <= args[0][2] <= 2030:
            return args
        else:
            print('Вы ввели некорректную дату')


d = Date('31-12-2021')
print(d.day)
