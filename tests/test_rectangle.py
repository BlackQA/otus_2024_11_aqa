from src.rectangle import Rectangle
import pytest


def test_rectangle_area_positive_integers():
    side_a = 3
    side_b = 5
    rectangle = Rectangle(side_a, side_b)
    assert (
        rectangle.get_area == 15
    ), "площадь прямоугольника со сторонами 3 и 5 должна составлять 15"


def test_rectangle_area_positive_floats():
    side_a = 3.5
    side_b = 5.5
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.get_area == pytest.approx(
        19.25
    ), "площадь прямоугольника со сторонами 3.5 и 5.5 должна составлять 19.5"


def test_rectangle_perimeter_positive_integers():
    side_a = 3
    side_b = 5
    rectangle = Rectangle(side_a, side_b)
    assert (
        rectangle.get_perimeter == 16
    ), "периметр прямоугольника со сторонами 3 и 5 должен составлять 16"


def test_rectangle_perimeter_positive_floats():
    side_a = 3.5
    side_b = 5.5
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.get_perimeter == pytest.approx(
        18
    ), "периметр прямоугольника со сторонами 3.5 и 5.5 должен составлять 18"


def test_rectangle_negative_side():
    with pytest.raises(ValueError) as exc_info:
        Rectangle(-1, 5)
    assert "can't be less than 0" in str(exc_info.value)


def test_rectangle_zero_side():
    with pytest.raises(ValueError) as exc_info:
        Rectangle(0, 5)
    assert "can't be less than 0" in str(exc_info.value)


def test_rectangle_non_numeric_input():
    with pytest.raises(TypeError):
        Rectangle("a", 5)
