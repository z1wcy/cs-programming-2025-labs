print("task_1")

numbers = [2, 6, 4, 3, 11, 88, 908, 55, 6, 97]
print("Исходный список:", numbers)

for i in range(len(numbers)):
    if numbers [i] == 3:
        numbers[i] = 30
print("Измененный список:", numbers)


print("task_2")

numbers = [2, 7, 5, 3, 8]

print(*map(lambda x: x**2, numbers))

print("task_3")

numbers = [0, 9, 54, 444, 88, 13, 66, 99]
result = max(numbers)/len(numbers)

print(f"Результат {result}")


print("task_4")

def sort_tuple(t):

    numbers = [x for x in t if isinstance(x, (int, float))]
    return tuple(sorted(numbers))


x = [9, 0.66, "indifference", "apps", 99, 14, None, 'True']
result = sort_tuple(tuple(x))
print(result)  


print("task_5")

def help(products):
    min1=min(products, key=products.get)
    max1=max(products, key=products.get)
    return min1, max1
products={"milk":120,"bread":50,"pie":220,"beer":90, "eggs":150}
print(help(products))


print("task_6")

list = [22, 'tv', 2.11, 'wow', True, 33, [1,2], None]
fool = dict()
for i in list:
    try:
        fool[i] = i
    except:
        pass
print(fool)


print("task_7")

eng_to_rus = {
    "sea":"море",
    "air":"воздух",
    "sky":"небо",
    "sun":"солнце",
    "moon":"луна",
    "rain":"дождь"
}

def find_english_translation(russian_word):
    
    for english, russian in eng_to_rus.items():
        if russian == russian_word:
            return english
    return "Перевод не найден"

word = input("Введите русское слово: ")
result = find_english_translation(word.lower())
print(f"Английский перевод: {result}")


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
        user = input("Ваш выбор (камень/ножницы/бумага/ящерица/спок/выход): ").lower()
        
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


print("task_9")

words = ["яблоко", "груша", "банан", "киви", "апельсин", "ананас"]

word_dict = {}
for word in words:
    f_letter = word[0]
    if f_letter not in word_dict:
        word_dict[f_letter] = []
    word_dict[f_letter].append(word)

print("Словарь по первой букве:")
print(word_dict)

print("task_10")

students = [("Анна", [5, 4, 5]), ("Иван", [3, 4, 4]), ("Мария", [5, 5, 5])]

avg_grades = {name: sum(grades)/len(grades) for name, grades in students}

best_name = ""
best_avg = 0
for name, avg in avg_grades.items():
    if avg > best_avg:
        best_avg = avg
        best_name = name

print(f"Лучший студент: {best_name} со средним баллом {best_avg:.2f}")