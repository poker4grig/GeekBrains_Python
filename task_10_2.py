# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
# одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать абстрактные
# классы для основных классов проекта и проверить работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    title = 'одежда'

    _all_cloth_count = 0

    @property
    def show_all_cloth_count(self):
        return f'на пошив всей одежы требуется {Clothes._all_cloth_count:.02f} метров ткани'

    @abstractmethod
    def __str__(self):
        return self.title


class Coat(Clothes):
    title = 'пальто'

    def __init__(self, value):
        self.value = value
        self.cloth_consumption = self.value / 6.5 + 0.5
        Clothes._all_cloth_count += self.cloth_consumption

    def __str__(self):
        return f'на пошив одежды типа {self.title} размера {self.value} необходимо {self.cloth_consumption:.2f} метров ткани'

    def __add__(self, other):
        return f'на пошив двух экземпляров одновременно требуется {self.cloth_consumption + other.cloth_consumption:.02f} метров ткани'


class Costume(Clothes):
    title = 'костюм'

    def __init__(self, height):
        self.height = height
        self.cloth_consumption = 2 * self.height + 0.3
        Clothes._all_cloth_count += self.cloth_consumption

    def __str__(self):
        return f'на пошив одежды типа {self.title} роста {self.height} необходимо {self.cloth_consumption:.2f} метров ткани'


coat = Coat(56)
print(coat)
costume = Costume(5)
print(costume)
print(coat + costume)
print(costume.show_all_cloth_count)
