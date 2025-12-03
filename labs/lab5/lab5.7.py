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