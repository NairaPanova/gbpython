delimiter = 60

time_sec = int(input("Введите время в секундах >>> "))

hour = time_sec//(delimiter**2)

minute = (time_sec%(delimiter**2))//delimiter

second = (time_sec%(delimiter**2))%delimiter

print("%02d:%02d:%02d" % (hour, minute, second))
