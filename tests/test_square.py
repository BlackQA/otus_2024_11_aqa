from src.square import Square
import pytest


def test_square_area_positive_integer():
    side = 5
    square = Square(side)
    expected_area = side**2
    assert square.get_area() == expected_area


def test_square_area_positive_float():
    side = 3.5
    square = Square(side)
    expected_area = side**2
    assert square.get_area() == pytest.approx(expected_area)


def test_square_perimeter_positive_integer():
    side = 5
    square = Square(side)
    expected_perimeter = 4 * side
    assert square.get_perimeter() == expected_perimeter


def test_square_perimeter_positive_float():
    side = 3.5
    square = Square(side)
    expected_perimeter = 4 * side
    assert square.get_perimeter() == pytest.approx(expected_perimeter)


def test_square_negative_side():
    with pytest.raises(ValueError) as exc_info:
        Square(-1)
    assert "can't be less than 0" in str(exc_info.value)


def test_square_zero_side():
    with pytest.raises(ValueError) as exc_info:
        Square(0)
    assert "can't be less than 0" in str(exc_info.value)


def test_square_non_numeric_input():
    with pytest.raises(TypeError):
        Square("a")
