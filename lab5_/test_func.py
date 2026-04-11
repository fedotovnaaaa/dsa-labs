import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides


class TestGetTriangleType(unittest.TestCase):
    # Равносторонний треугольник
    def test_equilateral(self):
        self.assertEqual(get_triangle_type(5, 5, 5), "equilateral")

    # Равнобедренный треугольник
    def test_isosceles(self):
        self.assertEqual(get_triangle_type(5, 5, 6), "isosceles")

    # Разносторонний треугольник
    def test_nonequilateral(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")

    # Плавающие числа 
    def test_floats(self):
        self.assertEqual(get_triangle_type(3.0, 4.0, 5.0), "nonequilateral")

    # Нарушение неравенства треугольника
    def test_invalid_inequality(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 3)

    # Отрицательная длина стороны
    def test_invalid_negative(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 2, 3)

    # Нулевая длина стороны
    def test_invalid_zero(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 1, 2)
    
    # Некорректный тип данных
    def test_invalid_type(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type("a", 1, 2)


if __name__ == "__main__":
    unittest.main()
