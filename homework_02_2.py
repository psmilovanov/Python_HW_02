# Задание 2.
x = 0
user_list = []
print("Вводите поочереди элементы списка. Для завершения ввода введите exit")

while x != "exit":
    x = input("Введите очередное значение списка: ")
    if x == "exit":
        break
    user_list.append(x)

print(user_list)
i = 0
while i < len(user_list) - 1:
    i += 1
    user_list[i], user_list[i - 1] = user_list[i - 1], user_list[i]
    i += 1
print(user_list)
