print("task_1")

numbers = [2, 6, 4, 3, 11, 88, 908, 55, 6, 97]
print("Исходный список:", numbers)

for i in range(len(numbers)):
    if numbers[i] == 3:
        numbers[i] = 30
print("Измененный список:", numbers)