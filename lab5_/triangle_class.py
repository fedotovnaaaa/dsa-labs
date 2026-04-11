from triangle_func import get_triangle_type, IncorrectTriangleSides


class Triangle:
    def __init__(self, a, b, c):
        # Используем готовую функцию для валидации
        get_triangle_type(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def triangle_type(self):
        # Возвращает тип треугольника
        return get_triangle_type(self.a, self.b, self.c)

    def perimeter(self):
        # Возвращает периметр треугольника
        return self.a + self.b + self.c
