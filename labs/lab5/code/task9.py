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