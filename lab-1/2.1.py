text = input()

# Разбиваем строку на слова (по пробелам)
words = text.split()

count_m = 0

for word in words:
    if word.startswith('m') or word.startswith('M'):
        count_m += 1

print(f"Количество слов, начинающихся с буквы 'm' или 'M': {count_m}")
