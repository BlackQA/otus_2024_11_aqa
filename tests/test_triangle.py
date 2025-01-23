from src.triangle import Triangle
import pytest


def test_triangle_area_positive_integers():
    a, b, c = 3, 4, 5
    triangle = Triangle(a, b, c)
    expected_area = 6.0
    assert (
        triangle.get_area == expected_area
    ), "площадь треугольника со сторонами 3, 4 и 5 должна составлять 6"


def test_triangle_area_positive_floats():
    a, b, c = 3.5, 4.5, 5.5
    triangle = Triangle(a, b, c)
    expected_area = pytest.approx(7.854, rel=1e-3)
    assert (
        triangle.get_area == expected_area
    ), "площадь треугольника со сторонами 3.5, 4.5 и 5.5 должна составлять 7.854"


def test_triangle_perimeter_positive_integers():
    a, b, c = 3, 4, 5
    triangle = Triangle(a, b, c)
    expected_perimeter = 12
    assert (
        triangle.get_perimeter == expected_perimeter
    ), "периметр треугольника со сторонами 3, 4 и 5 должен составлять 12"


def test_triangle_perimeter_positive_floats():
    a, b, c = 3.5, 4.5, 5.5
    triangle = Triangle(a, b, c)
    expected_perimeter = 13.5
    assert (
        triangle.get_perimeter == expected_perimeter
    ), "периметр треугольника со сторонами 3.5, 4.5 и 5.5 должен составлять 13.5"


def test_triangle_invalid_sides():
    with pytest.raises(ValueError) as exc_info:
        Triangle(1, 2, 3)
    assert "does not exist" in str(exc_info.value)


def test_triangle_negative_side():
    with pytest.raises(ValueError) as exc_info:
        Triangle(-1, 2, 3)
    assert "does not exist" in str(exc_info.value)


def test_triangle_zero_side():
    with pytest.raises(ValueError) as exc_info:
        Triangle(0, 2, 3)
    assert "does not exist" in str(exc_info.value)


def test_triangle_non_numeric_input():
    with pytest.raises(TypeError):
        Triangle("a", 2, 3)
