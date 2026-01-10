#task 10

try:
    number = int(input("Введите число: "))

    if number <= 1:
        print(f"{number} - Не является простым числом (простое число должно быть больше 1)")
    elif number == 2:
        print(f"{number} - Простое число")
    elif number % 2 == 0:
        print(f"{number} - Составное число")
    else:
        lit = True
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                lit = False
                break

        if lit:
            print(f"{number} - Простое число")
        else:
            print(f"{number} - Составное число")

except ValueError:
    print("Ошибка! Пожалуйста, введите целое число.")
except Exception as e:
    print(f"Произошла ошибка: {e}")