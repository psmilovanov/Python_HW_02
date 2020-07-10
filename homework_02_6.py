# Задание 6.

goods = []

dict_goods = {"название": [], "цена": [], "количество": [], "ед.": []}
dict_goods_set = {"название": {}, "цена": {}, "количество": {}, "ед.": {}}

quit = ''
i = 0
while True:
    quit = input("Для завершения ввода в структуру нажмите q. Любой другая клавиша приведет к вводу данных: ")
    if quit != 'q':

        dict_goods_curr = \
            {"название": None, "цена": None, "количество": None,
             "ед.": None}  # обнуление текущего словаря

        for key_goods in dict_goods_curr:
            name = input(f"Введите {key_goods} товара: ")
            if (key_goods == "цена") or (key_goods == "количество"):
                name = int(name)
            dict_goods_curr.update({key_goods: name})  # составление текущего словаря
            dict_goods.get(key_goods).append(name)  # составление общего словаря со списками

        i += 1
        z = (i, dict_goods_curr)  # составление кортежа
        goods.append(z)  # добавление кортежа в структуру

    else:
        break

print("Требуемая структура: ")
print(goods)

for key_goods in dict_goods:
    z = set(dict_goods.get(key_goods))
    dict_goods_set.update({key_goods: z})  # составление словаря как множества

dict_goods.clear()  # обнуление словаря
print("Требуемый словарь")
print(dict_goods_set)
