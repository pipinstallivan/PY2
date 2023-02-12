from abc import ABC, abstractmethod


class Prizm:
    """базовый класс геометрических фигур-призм"""
    surface = None

    def __init__(self, color=None, depth=None):
        """инициализируемм экземпляр"""
        self.color = color  # цвет фигуры
        self.depth = depth  # высота призмы

    def __str__(self):
        """возвращает в удобной для чтения форме информацию об экземпляре"""
        return (f"{self.__class__.__name__}\n depth = {self.depth}\n Color = {self.color}")

    def __repr__(self):
        """возвращает готовое объявление экземпляра класса"""
        return (f"{self.__class__.__name__}({self.color}, {self.depth})")

    @property
    @abstractmethod
    # у каждой призмы объем вычисляется по-разному
    def volume(self):
        """Объем призмы у каждой - свой"""
        pass

    @property
    def surface_calc(self):
        """Вычисляет лощадь поверхности. можно считать, но можно не уточнять"""
        return self.surface


class Cylinder(Prizm):
    """Класс геометрических фигур-цилиндров"""

    def __init__(self, r: float, color: float, depth: float):
        super().__init__(color, depth)
        self.r = r

    def volume(self):
        """Возврящает объем цилиндра"""
        return 3.14 * (self.depth ** 2) * self.depth


if __name__ == "__main__":
    # Write your solution here
    fig1 = Prizm(1, 2)
    print(fig1)
    print(repr(fig1))
    print(fig1.surface)
    fig2 = Cylinder(2, 1, 2)
    print(fig2)
    print(repr(fig2))
    print(fig2.volume())
    print(fig2.surface_calc)
