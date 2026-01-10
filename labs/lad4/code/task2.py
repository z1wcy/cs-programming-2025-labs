#task2

def season (num):
    if num < 1 or num > 12:
        print("Ошибка: Введите число от 1 до 12")
    elif num in [1, 2, 12]:
        print("Это зима! ")
    elif num in [3, 4, 5]:
        print("Это весна! ")
    elif num in [6, 7, 8]:
        print("Это лето! ")
    else:
        print("Это осень! ")

num = int(input(" Введите номер месяца (1-12): "))
season (num)
