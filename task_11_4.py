# 4. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку методов
# сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
class ComplexNumber:

    def __init__(self, name):
        self.c_number = name

    def __add__(self, other):
        return f'результат сложения комплексных чисел равняется: {self.c_number + other.c_number}'

    def __sub__(self, other):
        return f'результат вычитания комплексных чисел равняется: {self.c_number - other.c_number}'

    def __mul__(self, other):
        return f'результат умножения комплексного числа на комплексное или вещественное число равняется: {self.c_number * other.c_number}'


cn_1 = ComplexNumber(9 + 5j)
cn_2 = ComplexNumber(5 + 7j)
# cn_2 = ComplexNumber(5)
print(cn_1 + cn_2)
print(cn_1 - cn_2)
print(cn_1 * cn_2)
# сложение complex (a+bi)+(c+di)=(a+c)+(b+d)i
# умножение complex на complex (a+bi)⋅(c+di)=(ac−bd)+(bc+ad)i
