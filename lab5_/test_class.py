import pytest
from triangle_class import Triangle
from triangle_func import IncorrectTriangleSides


def test_triangle_creation_positive_nonequilateral():
    # Создание разностороннего треугольника + проверка методов
    t = Triangle(3, 4, 5)
    assert t.triangle_type() == "nonequilateral"
    assert t.perimeter() == 12


def test_triangle_creation_equilateral():
    # Равносторонний треугольник
    t = Triangle(5, 5, 5)
    assert t.triangle_type() == "equilateral"
    assert t.perimeter() == 15


def test_triangle_creation_isosceles():
    # Равнобедренный треугольник
    t = Triangle(5, 5, 6)
    assert t.triangle_type() == "isosceles"
    assert t.perimeter() == 16


def test_triangle_creation_floats():
    # + тест: плавающие числа
    t = Triangle(3.0, 4.0, 5.0)
    assert t.triangle_type() == "nonequilateral"
    assert t.perimeter() == 12.0


def test_invalid_creation_inequality():
    # - тест: нарушение неравенства треугольника
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 3)


def test_invalid_creation_negative():
    # - тест: отрицательная сторона
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, 2, 3)


def test_invalid_creation_zero():
    # - тест: нулевая сторона
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 1, 2)


def test_invalid_creation_type():
    # - тест: некорректный тип данных
    with pytest.raises(IncorrectTriangleSides):
        Triangle("a", 1, 2)


def test_perimeter_method():
    # Тест метода perimeter для разностороннего треугольника
    t = Triangle(3, 4, 5)
    assert t.perimeter() == 12
