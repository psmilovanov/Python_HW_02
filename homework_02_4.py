# Задание 4.

user_str = input("Введите строку: ")
user_str = user_str.split()

i = 0
for el in user_str:
    i += 1
    print(f"Строка {i}", el[:10])
