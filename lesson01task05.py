earnings = float(input("Введите сумму выручки >>> "))
costs = float(input("Введите сумму издержек >>> "))

if earnings <= costs:
    loss = costs - earnings
    print("Убыток составил:", loss)
    print("Прибыль составила: 0")

else:
    profit = earnings - costs
    print("Прибыль составила:", profit)
    profitability = round((profit / earnings), 2)
    print("Рентабельность составила:", profitability)

    number_of_employees = int(input("Введите численность сотрудников фирмы >>> "))

    profit_per_employee = round(profit / number_of_employees, 2)
    print("Прибыль на одного сотрудника составила:", profit_per_employee)


