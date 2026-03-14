try:
    a = float(input())
    b = float(input())
    c = float(input())

    print("Числа, попадающие в интервал [1, 50]:")

    if 1 <= a <= 50:
        print(a)

    if 1 <= b <= 50:
        print(b)

    if 1 <= c <= 50:
        print(c)
except ValueError:
    print('Ошибка! Нужно вводить числа')
