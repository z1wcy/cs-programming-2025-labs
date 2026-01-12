def calculate_profit(a, n):
    if a < 30000: return "Ошибка: минимальная сумма 30 000 руб."
    
    term = 0.03 if n <= 3 else 0.05 if n <= 6 else 0.02
    sum = min((a // 10000) * 0.003, 0.05)
    
    profit = a * (1 + term + sum) ** n - a
    return f"Прибыль: {round(profit, 2):,.2f} руб."

def main_compact():
    print("Калькулятор вклада (сумма, срок):")
    while True:
        try:
            data = input("Ввод: ").split()
            if len(data) != 2: continue
            
            amount, years = float(data[0]), int(data[1])
            result = calculate_profit(amount, years)
            print(result)
            
        except (ValueError, IndexError):
            print("Ошибка ввода!")
        except KeyboardInterrupt:
            print("\nВыход"); break

main_compact()