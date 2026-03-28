try:
    m = float(input())

    for i in range(1, 11):
        result = i * m
        print(f"{i} × {m} = {result}")
except ValueError:
    print('Ошибка! Нужно вводить числа')
