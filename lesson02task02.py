length = input("Введите число элементов в создаваемом списке >>> ")

if not length.isdigit():
    print("Неверный формат числа")
    exit()

length = int(length)

user_list = []

while len(user_list) < int(length):
    user_el = input("Введите элемент списка >>> ")
    user_list.append(user_el)

print("Список:", user_list)

index = 0

while index < length - 1:
    user_list[index], user_list[index + 1] = user_list[index + 1], user_list[index]
    index += 2


print("Новый список:", user_list)
