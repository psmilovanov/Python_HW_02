# Задание 3.

seasons = ['зима', 'весна', 'лето', 'осень']
seasons_dict = {0: "зима", 1: "весна", 2: "лето", 3: "осень"}
print(seasons_dict.get(1))
print("Для окончания работы программы введите 0")

while True:
    x = int(input("Введите номер месяца: "))
    if x == 0:
        break
    else:
        i = (x % 12) // 3
        print(f"Месяц с номером {x} это {seasons[i]}")
        print(f"и полученная через словарь значение {seasons_dict.get(i)}")
