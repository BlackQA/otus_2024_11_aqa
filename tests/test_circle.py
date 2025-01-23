from src.circle import Circle
import math
import pytest


def test_circle_area_positive_integer():
    radius = 3
    circle = Circle(radius)
    expected_area = math.pi * radius**2
    assert circle.get_area() == pytest.approx(expected_area)


def test_circle_area_positive_float():
    radius = 2.5
    circle = Circle(radius)
    expected_area = math.pi * radius**2
    assert circle.get_area() == pytest.approx(expected_area)


def test_circle_perimeter_positive_integer():
    radius = 3
    circle = Circle(radius)
    expected_perimeter = 2 * math.pi * radius
    assert circle.get_perimeter() == pytest.approx(expected_perimeter)


def test_circle_perimeter_positive_float():
    radius = 2.5
    circle = Circle(radius)
    expected_perimeter = 2 * math.pi * radius
    assert circle.get_perimeter() == pytest.approx(expected_perimeter)


def test_circle_negative_radius():
    with pytest.raises(ValueError) as exc_info:
        Circle(-1)
    assert "cannot be less than or equal to zero" in str(exc_info.value)


def test_circle_zero_radius():
    with pytest.raises(ValueError) as exc_info:
        Circle(0)
    assert "cannot be less than or equal to zero" in str(exc_info.value)


def test_circle_non_numeric_input():
    with pytest.raises(TypeError):
        Circle("a")
