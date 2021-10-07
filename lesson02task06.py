id_quantity = input("Введите количество наименований товаров >>> ")

if not id_quantity.isdigit():
    print("Неверный формат числа")
    exit()

id_quantity = int(id_quantity)

goods_list = []

name_key = "Название"
price_key = "Цена"
quantity_key = "Количество"
units_key = "Единица измерения"

good_id = 1

while good_id <= id_quantity:
    name = input("Введите наименование товара >>> ")
    price = float(input("Введите цену товара >>> "))
    quantity = int(input("Введите количество товара >>> "))
    units = input("Введите единицу измерения количества товара >>> ")

    good_inf = (good_id, {name_key: name, price_key: price, quantity_key: quantity, units_key: units})

    goods_list.append(good_inf)
    good_id += 1
else:

    print("Товары:", goods_list)

name_list = []
price_list = []
quantity_list = []
units_list = []

for el in goods_list:
    name_list.append(el[1].get(name_key))
    price_list.append(el[1].get(price_key))
    quantity_list.append(el[1].get(quantity_key))
    units_list.append(el[1].get(units_key))

goods_dict = {name_key: name_list, price_key: price_list, quantity_key: quantity_list, units_key: units_list}

print("Аналитика:", goods_dict)
