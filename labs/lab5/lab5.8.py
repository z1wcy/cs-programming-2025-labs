print("task_8")

import random

def simple_game():
    choices = ["камень", "ножницы", "бумага", "ящерица", "спок"]
    
    rules = {
        "камень": ["ножницы", "ящерица"],
        "ножницы": ["бумага", "ящерица"],
        "бумага": ["камень", "спок"],
        "ящерица": ["бумага", "спок"],
        "спок": ["камень", "ножницы"]
    }
    
    while True:
        user = input("Ваш выбор (камень, ножницы,бумага, ящерица, спок, выход): ").lower()
        
        if user == "выход":
            break
        if user not in choices:
            print("Неверный выбор!")
            continue
            
        computer = random.choice(choices)
        print(f"Компьютер выбирает: {computer}")
        
        if user == computer:
            print("Ничья!")
        elif computer in rules[user]:
            print("Вы выиграли!")
        else:
            print("Компьютер выиграл!")

simple_game()