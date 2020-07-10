# Задание 5.

origin_list = [14, 7, 5, 5, 2, 1]
print(f" Исходный набор {origin_list}")
print("Добавляйте натуральное число. Для выхода из программы введите 0")
while True:
    x = int(input("Введите натуральное число: "))
    if x != 0:
        origin_list.append(x)
        origin_list.sort()
        origin_list.reverse()
        print(f"Новый набор {origin_list}")
    else:
        break
