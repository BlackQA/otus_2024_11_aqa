from src.circle import Circle
from src.square import Square
import math
import pytest


@pytest.mark.parametrize("radius", [3, 2.5],
                         ids=["integer", "float"])
def test_circle_area_positive(radius):
    circle = Circle(radius)
    expected_area = math.pi * radius**2
    assert circle.get_area == pytest.approx(expected_area)


@pytest.mark.parametrize("radius", [3, 2.5],
                         ids=["integer", "float"])
def test_circle_perimeter_positive(radius):
    circle = Circle(radius)
    expected_perimeter = 2 * math.pi * radius
    assert circle.get_perimeter == pytest.approx(expected_perimeter)


@pytest.mark.parametrize(
    "radius, expected_exception",
    [
        (-1, ValueError),
        (-2.5, ValueError),
        (0, ValueError),
    ],
    ids=["negative_integer", "negative_float", "zero"],
)
def test_circle_negative_or_zero(radius, expected_exception):
    with pytest.raises(expected_exception) as exc_info:
        Circle(radius)
    assert "cannot be less than or equal to zero" in str(exc_info.value)


@pytest.mark.parametrize("radius", ["a", [1, 2]],
                         ids=["string", "list"])
def test_circle_string_type(radius):
    with pytest.raises(TypeError):
        Circle(radius)


@pytest.mark.parametrize("other_radius", [4, 5.5],
                         ids=["other_integer", "other_float"])
def test_circle_add_area_with_circle(other_radius):
    circle1 = Circle(3)
    circle2 = Circle(other_radius)
    total_area = circle1.add_area(circle2)
    expected_total_area = circle1.get_area + circle2.get_area
    assert total_area == pytest.approx(expected_total_area)


@pytest.mark.parametrize("side", [4, 5.5],
                         ids=["side_integer", "side_float"])
def test_circle_add_area_with_square(side):
    circle = Circle(3)
    square = Square(side)
    total_area = circle.add_area(square)
    expected_total_area = circle.get_area + square.get_area
    assert total_area == pytest.approx(expected_total_area)
