from src.square import Square
from src.circle import Circle
import pytest


@pytest.mark.parametrize("side", [3, 2.5],
                         ids=["integer", "float"])
def test_square_area_positive(side):
    square = Square(side)
    expected_area = side**2
    assert square.get_area == pytest.approx(expected_area)


@pytest.mark.parametrize("side", [3, 2.5],
                         ids=["integer", "float"])
def test_square_perimeter_positive(side):
    square = Square(side)
    expected_perimeter = 4 * side
    assert square.get_perimeter == pytest.approx(expected_perimeter)


@pytest.mark.parametrize(
    "side, expected_exception",
    [(-1, ValueError), (-2.5, ValueError), (0, ValueError)],
    ids=["negative_integer", "negative_float", "zero"],
)
def test_square_negative_or_zero(side, expected_exception):
    with pytest.raises(expected_exception) as exc_info:
        Square(side)
    assert "can't be less than 0" in str(exc_info.value)


@pytest.mark.parametrize("side", ["a", [1, 2]],
                         ids=["string", "list"])
def test_square_string_type(side):
    with pytest.raises(TypeError):
        Square(side)


@pytest.mark.parametrize("radius", [4, 5.5],
                         ids=["radius_integer", "radius_float"])
def test_square_add_area_with_circle(radius):
    square = Square(3)
    circle = Circle(radius)
    total_area = square.add_area(circle)
    expected_total_area = square.get_area + circle.get_area
    assert total_area == pytest.approx(expected_total_area)


@pytest.mark.parametrize("other_side", [4, 5.5],
                         ids=["other_integer", "other_float"])
def test_square_add_area_with_square(other_side):
    square1 = Square(3)
    square2 = Square(other_side)
    total_area = square1.add_area(square2)
    expected_total_area = square1.get_area + square2.get_area
    assert total_area == pytest.approx(expected_total_area)
