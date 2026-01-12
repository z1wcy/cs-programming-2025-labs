objects = [
    ("Containment Cell A", 4),
    ("Archive Vault", 1),
    ("Bio Lab Sector", 3),
    ("Observation Wing", 2)
]

sorted_objects = sorted(objects, key=lambda item: item[1])

print("Объекты по возрастанию уровня угрозы: ")
print(sorted_objects)