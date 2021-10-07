user_input = input("Введите несколько слов через пробел >>> ")

new_list = user_input.split(" ")

index = 1

for el in new_list:
    print(index, el[0:10])
    index += 1
