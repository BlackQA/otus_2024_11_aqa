from src.rectangle import Rectangle
from src.triangle import Triangle
import pytest


@pytest.mark.parametrize(
    "side_a, side_b", [(3, 4), (2.5, 5.5)],
    ids=["integer_sides", "float_sides"]
)
def test_rectangle_area_positive(side_a, side_b):
    rectangle = Rectangle(side_a, side_b)
    expected_area = side_a * side_b
    assert rectangle.get_area == pytest.approx(expected_area)


@pytest.mark.parametrize(
    "side_a, side_b", [(3, 4), (2.5, 5.5)],
    ids=["integer_sides", "float_sides"]
)
def test_rectangle_perimeter_positive(side_a, side_b):
    rectangle = Rectangle(side_a, side_b)
    expected_perimeter = (side_a + side_b) * 2
    assert rectangle.get_perimeter == pytest.approx(expected_perimeter)


@pytest.mark.parametrize(
    "side_a, side_b, expected_exception",
    [(-1, 4, ValueError), (3, -4.5, ValueError), (0, 4, ValueError)],
    ids=["negative_integer", "negative_float", "zero"],
)
def test_rectangle_negative_or_zero(side_a, side_b, expected_exception):
    with pytest.raises(expected_exception) as exc_info:
        Rectangle(side_a, side_b)
    assert "can't be less than 0" in str(exc_info.value)


@pytest.mark.parametrize(
    "side_a, side_b", [("a", 4), (3, [1, 2])],
    ids=["string", "list"]
)
def test_rectangle_string_type(side_a, side_b):
    with pytest.raises(TypeError):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize(
    "side_a, side_b",
    [(4, 5), (5.5, 6.5)],
    ids=["rectangle_integer_sides", "rectangle_float_sides"],
)
def test_triangle_add_area_with_rectangle(side_a, side_b):
    rectangle = Rectangle(side_a, side_b)
    triangle = Triangle(3, 4, 5)
    total_area = rectangle.add_area(triangle)
    expected_total_area = rectangle.get_area + triangle.get_area
    assert total_area == pytest.approx(expected_total_area)


@pytest.mark.parametrize(
    "other_side_a, other_side_b",
    [(4, 5), (5.5, 6.5)],
    ids=["other_integer_sides", "other_float_sides"],
)
def test_rectangle_add_area_with_rectangle(other_side_a, other_side_b):
    rectangle1 = Rectangle(3, 4)
    rectangle2 = Rectangle(other_side_a, other_side_b)
    total_area = rectangle1.add_area(rectangle2)
    expected_total_area = rectangle1.get_area + rectangle2.get_area
    assert total_area == pytest.approx(expected_total_area)
