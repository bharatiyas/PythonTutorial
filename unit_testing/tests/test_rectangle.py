import pytest
import source.shapes as shapes


def test_area():
    rectangle = shapes.Rectangle(10, 2)
    assert rectangle.area() == 10 * 2


def test_perimeter():
    rectangle = shapes.Rectangle(10, 2)
    assert rectangle.perimeter() == 2 * (10 + 2)
