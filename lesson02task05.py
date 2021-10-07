rating = []

while True:
    user_input = input("Введите натуральное число >>> ")

    if not user_input.isdigit():
        print("Неверный формат числа")
        exit()

    user_input = int(user_input)

    rating.append(user_input)
    rating.sort(reverse=True)
    print(rating)
