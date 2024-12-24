from abc import ABC, abstractmethod

class Figure(ABC):
    @property
    def get_area(self):
        pass

    @property
    def get_perimeter(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
             raise ValueError("Should be a Figure")
        return self.get_area + other_figure.get_area