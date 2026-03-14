try:
    summa = 0
    count = 0

    while True:
        num = input()
        if num == '':
            break
        summa += int(num)
        count += 1

    print(f'Сумма чисел: {summa}')
    print(f'Кол-во чисел: {count}')
except ValueError:
    print('Ошибка! Нужно вводить числа (через enter)')
