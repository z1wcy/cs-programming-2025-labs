evaluations = [
    {"name": "Agent Cole", "score": 78},
    {"name": "Dr. Weiss", "score": 92},
    {"name": "Technician Moore", "score": 61},
    {"name": "Researcher Lin", "score": 88}
]

top_eval = max(evaluations, key=lambda x: x["score"])
result = f"{top_eval['name']} - {top_eval['score']}"

print("Сотрудник с наивысшей психологической оценкой: ")
print(result)