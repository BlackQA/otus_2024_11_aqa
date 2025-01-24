from figure import Figure
import math


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if (
            not (
                side_a + side_b > side_c
                and side_a + side_c > side_b
                and side_b + side_c > side_a
            )
            or side_a <= 0
            or side_b <= 0
            or side_c <= 0
        ):
            raise ValueError("A triangle with such sides does not exist")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def get_area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
