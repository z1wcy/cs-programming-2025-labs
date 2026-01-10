#task1

def air_conditioner():
    if temp >= 20:
        print("Кондиционер выключается")
    else:
        print("Кондиционер включается")

temp = float(input("Введите температуру в помещении: "))
air_conditioner()