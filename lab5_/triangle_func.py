# Исключение, выбрасывается при некорректных сторонах треугольника
class IncorrectTriangleSides(Exception):
    pass


def get_triangle_type(a, b, c):
    # Проверка типов и корректности сторон
    if not all(isinstance(side, (int, float)) for side in (a, b, c)):
        raise IncorrectTriangleSides
    # Проверка неравенства треугольника и положительности сторон
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides

    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "nonequilateral"

if __name__ == "__main__":
    # Пример использования функции
    try:
        print(get_triangle_type(3, 4, 5))
        print(get_triangle_type(5, 5, 5))
        print(get_triangle_type(5, 5, 6))
        print(get_triangle_type(-1, 2, 3))
    except IncorrectTriangleSides:
        print("Некорректные стороны треугольника.")
