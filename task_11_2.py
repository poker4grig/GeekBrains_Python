# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных, вводимых
# пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
class ZerroDivErr(Exception):
    def __str__(self):
        return f'{ZerroDivErr.__name__}: деление на ноль запрещено'


a, b = (int(i) for i in input('Введите два числа, первое - делимое, второе - делитель: ').split()) #попробовал необычный способ ввода чисел


def divizion(a, b):
    try:
        if b == 0:
            raise ZerroDivErr
    except ZerroDivErr as e:
        print(e)
    else:
        return a / b


print(divizion(a, b))
