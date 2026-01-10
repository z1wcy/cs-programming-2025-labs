#task 9

def time (num):
    if num < 0 or num > 23:
        print("Ошибка: Введите число от 0 до 23")
    elif num in [0, 1, 2, 3, 4, 5]:
        print("Это ночь! ")
    elif num in [6, 7, 8, 9, 10, 11]:
        print("Это утро! ")
    elif num in [12, 13, 14, 15, 16, 17]:
        print("Это день! ")
    else:
        print("Это вечер! ")

num = int(input(" Введите время суток (0-23): "))
time (num)