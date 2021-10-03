number = int(input("Введите целое положительное число >>> "))

while number <= 0:
    number = int(input("Введите целое положительное число >>> "))

else:
    length = len(str(number))

    num_max = number//(10**(length-1))
    num_last = number%(10**(length-1))

    while len(str(num_last)) > 1:
        length = length - 1
        num_next = num_last // (10 ** (length - 1))
        num_max = max(num_max, num_next)
        num_last = num_last%(10**(length-1))

    else:
        num_max = max(num_max, num_last)
        print("Самая большая цифра в числе:", num_max)