from figure import Figure
import math

class Square(Figure):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Square sides can't be less than 0")
        self.side_a = side_a

    def get_area(self):
        return self.side_a ** 2

    def get_perimeter(self):
        return 4 * self.side_a