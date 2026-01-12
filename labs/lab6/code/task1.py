def time_convert():
   
    time = {
        's': 1, 'sec': 1, 'second': 1,
        'm': 60, 'min': 60, 'minute': 60,
        'h': 3600, 'hr': 3600, 'hour': 3600,
        'd': 86400, 'day': 86400
    }
    
    user_input = input("Введите время для конвертации: ")
    
    try:
        value, from_time, to_time = user_input.split()
        value = float(value)
        from_time = from_time.lower()
        to_time = to_time.lower()
        
        if from_time in time and to_time in time:
            result = value * time[from_time] / time[to_time]
            if result.is_integer():
                print(f"Результат: {int(result)}{to_time}")
            else:
                print(f"Результат: {result:.2f}{to_time}")
        else:
            print("Ошибка: неизвестная единица измерения.")
            
    except ValueError:
        print("Ошибка: неверный формат ввода.")

time_convert()