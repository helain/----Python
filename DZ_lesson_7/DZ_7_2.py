"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod
class Outfit(ABC):

    @abstractmethod
    def material_consumption(self):
        pass

class Coat(Outfit):
    def __init__(self, title, size):
        self.title = title
        self.size = size

    @property
    def material_consumption(self):
        material_consumption = self.size/6.5 + 0.5
        return material_consumption

class Suit(Outfit):
    def __init__(self, title, height):
        self.title = title
        self.height = height

    @property
    def material_consumption(self):
        material_consumption = 2* self.height + 0.3
        return material_consumption


wool_coat = Coat('Wool coat', 50)
classic_suit = Suit('Classic suit', 50)

print(f'Для производства {wool_coat.title} и {classic_suit.title} '
      f'необходимо {wool_coat.material_consumption+classic_suit.material_consumption}')
