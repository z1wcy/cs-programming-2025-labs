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