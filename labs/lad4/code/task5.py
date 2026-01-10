#task 5

def check_password():
    print(" Проверка надежности пароля ")

    password = input("Введите пароль для проверки: ")

    conditions = {
        "Длина не менее 8 символов": len(password) >= 8,
        "Содержит заглавные буквы латиницы": any(c.isupper() for c in password),
        "Содержит строчные буквы латиницы": any(c.islower() for c in password),
        "Содержит цифры": any(c.isdigit() for c in password),
        "Содержит специальные знаки": any(not c.isalnum() for c in password)
    }

    print("\nРезультат проверки:")

    all_conditions_met = True
    for condition, met in conditions.items():
        status = "+ Выполнено" if met else "- Не выполнено"
        print(f"{status}: {condition}")

        if not met:
            all_conditions_met = False

    print(f"\nОбщий результат: {'+ Пароль надежный' if all_conditions_met else '- Пароль ненадежный'}")


check_password()