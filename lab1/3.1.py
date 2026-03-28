import sys

args_list = sys.argv[1:]

try:
    a = [int(arg) for arg in args_list]
    N = len(a)  # Вычисляем длину массива

    if N == 0:
        print("Ошибка: Массив не должен быть пустым")
        sys.exit(1)

    print(f"Исходный массив: {a}")

    max_element = a[0]
    for num in a:
        if num > max_element:
            max_element = num

    print(f"Максимальный элемент: {max_element}")

    reversed_a = a[::-1]
    print(f"Массив в обратном порядке: {reversed_a}")

    sum_elements = 0
    for num in a:
        sum_elements += num

    srednee = sum_elements / N
    print(f"Среднее арифметическое: {srednee}")

    result_a = []
    for num in a:
        if num == 0:
            result_a.append(srednee)
        else:
            result_a.append(num)

    print(f"Результат после замены нулей: {result_a}")

except ValueError:
    print("Ошибка: Все аргументы должны быть целыми числами")
except Exception as e:
    print(f"Произошла ошибка: {e}")
