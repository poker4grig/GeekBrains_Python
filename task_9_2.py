# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной
# в 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.
class Road:
    def __init__(self, length, width, asph_thickness):
        self._length = length
        self._width = width
        self.asph_mass = 25
        self.asph_thickness = asph_thickness

    def asphalt_mass(self):
        result = int(self._length * self._width * self.asph_mass * self.asph_thickness / 1000)
        return f'{result} т.'


r = Road(20, 5000, 5)
print(r.asphalt_mass())

