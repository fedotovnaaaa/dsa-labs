try:
    a = float(input())
    b = float(input())
    c = float(input())
    print(f'Минимальное число: {min(a, b, c)}')
except ValueError:
    print("Ошибка! Нужно вводить числа")
