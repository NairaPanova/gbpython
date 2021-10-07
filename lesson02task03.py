month_num = input("Введите номер месяца >>> ")

if not month_num.isdigit():
    print("Неверный формат числа")
    exit()

month_num = int(month_num)

season_dict = {"зима": [1, 2, 12], "весна": [3, 4, 5], "лето": [6, 7, 8], "осень": [9, 10, 11]}

for key in season_dict:
    if month_num in season_dict.get(key):
        print("Время года:", key)
    else:
        continue

