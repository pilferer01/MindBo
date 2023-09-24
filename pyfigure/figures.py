# Напишите на C# или Python библиотеку для поставки внешним клиентам, которая умеет вычислять площадь круга по радиусу и
# треугольника по трем сторонам. Дополнительно к работоспособности оценим:
# Юнит-тесты
# Легкость добавления других фигур
# Вычисление площади фигуры без знания типа фигуры в compile-time
# Проверку на то, является ли треугольник прямоугольным
# Я не понял, что значит для "поставки внешним клиентам". Типа в pip загрузить или документацию с примерами сделать?
# P.S. Я сделал документацию с примерами

import math
from abc import ABC, abstractmethod


class Figure(ABC):
    """Абстрактный класс"""

    def _check_existence(self, *args):
        """Проверка на существование фигуры"""
        for arg in args:
            if arg <= 0:
                raise ValueError(f'{arg} < 0')

    @abstractmethod
    def calculate_area(self):
        pass


class Triangle(Figure):
    """Управление треугольником
    Parameters:
        side_a:
            сторона А
        side_b:
            сторона Б
        side_c:
            сторона С
    """

    def __init__(self, side_a=None, side_b=None, side_c=None):
        if not (side_a or side_b or side_c):
            side_a = float(input("Entry side_a: "))
            side_b = float(input("Entry side_b: "))
            side_c = float(input("Entry side_c: "))
        self._check_existence(side_a, side_b, side_c)
        self.sideA = side_a
        self.sideB = side_b
        self.sideC = side_c

    def _check_existence(self, *args):
        """Проверка на существование треугольника"""
        super()._check_existence(*args)
        a, b, c = args
        if a + b < c or b + c < a or c + a < b:
            raise ValueError("One side of the triangle is greater than the sum of the other two sides. Such a triangle "
                             "cannot exist.")

    def check_right_triangle(self):
        """Проверка является ли треугольник прямоугольным"""
        if (self.sideA ** 2 + self.sideB ** 2 == self.sideC ** 2
                or self.sideB ** 2 + self.sideC ** 2 == self.sideA ** 2
                or self.sideC ** 2 + self.sideA ** 2 == self.sideB ** 2):
            return True
        return False

    def calculate_area(self):
        """Вычисление площади треугольника по трем сторонам"""
        p = (self.sideA + self.sideB + self.sideC) / 2
        return (p * (p - self.sideA) * (p - self.sideB) * (p - self.sideC)) ** 0.5


class Circle(Figure):
    """Управление кругом
    Parameters:
        r:
            радиус
    """

    def __init__(self, r=None):
        if not r:
            r = float(input("Entry radius: "))
        self._check_existence(r)
        self.r = r

    def calculate_area(self):
        """Вычисление площади круга по радиусу"""
        return math.pi * self.r ** 2


def unknown_figure():
    """Вычисление площади фигуры без знания типа фигуры"""
    while True:
        figure_name = input("\nEntry figure name: ")
        if figure_name.lower() == 'circle':
            # Я хотел возвращать объкт, но в задании сказано вычислять, поэтому я сделал так
            print(Circle().calculate_area())
            break
        elif figure_name.lower() == 'triangle':
            print(Triangle().calculate_area())
            break
