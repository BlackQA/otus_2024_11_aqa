from figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("The radius cannot be less than or equal to zero")
        self.radius = radius

    @property
    def get_area(self):
        return math.pi * self.radius**2

    @property
    def get_perimeter(self):
        return 2 * math.pi * self.radius
