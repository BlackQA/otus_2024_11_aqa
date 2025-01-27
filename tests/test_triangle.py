from src.triangle import Triangle
from src.rectangle import Rectangle
import pytest
import math


@pytest.mark.parametrize(
    "side_a, side_b, side_c", [(3, 4, 5), (5.5, 12.2, 13.6)],
    ids=["integer", "float"]
)
def test_triangle_area_positive(side_a, side_b, side_c):
    triangle = Triangle(side_a, side_b, side_c)
    s = (side_a + side_b + side_c) / 2
    expected_area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
    assert triangle.get_area == pytest.approx(expected_area)


@pytest.mark.parametrize(
    "side_a, side_b, side_c", [(3, 4, 5), (5.5, 12.2, 13.6)],
    ids=["integer", "float"]
)
def test_triangle_perimeter_positive(side_a, side_b, side_c):
    triangle = Triangle(side_a, side_b, side_c)
    expected_perimeter = side_a + side_b + side_c
    assert triangle.get_perimeter == expected_perimeter


@pytest.mark.parametrize(
    "side_a, side_b, side_c, expected_exception",
    [
        (1, 2, 3, ValueError),
        (0, 4, 5, ValueError),
        (1, -4, 5, ValueError),
        (1.5, 2.5, 4, ValueError),
        (0.0, 4.5, 5.5, ValueError),
        (1.5, -4.5, 5.5, ValueError),
    ],
    ids=[
        "invalid_integer",
        "invalid_integer_zero",
        "invalid_integer_negative",
        "invalid_float",
        "invalid_float_zero",
        "invalid_float_negative",
    ],
)
def test_triangle_negative_or_zero(side_a, side_b, side_c, expected_exception):
    with pytest.raises(expected_exception) as exc_info:
        Triangle(side_a, side_b, side_c)
    assert "does not exist" in str(exc_info.value)


@pytest.mark.parametrize(
    "side_a, side_b, side_c", [("a", 4, 5), (3, [1, 2], 5)],
    ids=["string", "list"]
)
def test_rectangle_string_type(side_a, side_b, side_c):
    with pytest.raises(TypeError):
        Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize(
    "side_a, side_b",
    [(4, 5), (5.5, 6.5)],
    ids=["rectangle_integer_sides", "rectangle_float_sides"],
)
def test_triangle_add_area_with_rectangle(side_a, side_b):
    triangle = Triangle(3, 4, 5)
    rectangle = Rectangle(side_a, side_b)
    total_area = triangle.add_area(rectangle)
    expected_total_area = triangle.get_area + rectangle.get_area
    assert total_area == pytest.approx(expected_total_area)


@pytest.mark.parametrize(
    "side_a, side_b, side_c",
    [(3, 4, 5), (5.5, 12.5, 13.5)],
    ids=["triangle1", "triangle2"],
)
def test_triangle_add_area_with_triangle(side_a, side_b, side_c):
    triangle1 = Triangle(3, 4, 5)
    triangle2 = Triangle(side_a, side_b, side_c)
    total_area = triangle1.add_area(triangle2)
    expected_total_area = triangle1.get_area + triangle2.get_area
    assert total_area == pytest.approx(expected_total_area)
