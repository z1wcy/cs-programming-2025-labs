#task 3

def dog_to_human_age():
    print(" Перевод собачьего возраста в человеческий ")
    try:
        dog_age = float(input("Введите возраст собаки: "))
        if dog_age < 1:
            print("Ошибка: Возраст собаки не может быть меньше 1 года")
            return
        if dog_age > 22:
            print("Ошибка: Слишком большой возраст для собаки (максимум 22 года)")
            return
        if dog_age <= 2:
            human_age = dog_age * 10.5
        else:
            human_age = 2 * 10.5 + (dog_age - 2) * 4

        print(f"Собачий возраст: {dog_age} лет")
        print(f"Эквивалентный человеческий возраст: {human_age} лет")

    except ValueError:
        print("Ошибка: Введите возраст собаки числом")


dog_to_human_age()