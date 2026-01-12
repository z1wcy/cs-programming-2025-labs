staff_shifts = [
    {"name": "Dr. Shaw", "shift_cost": 120, "shifts": 15},
    {"name": "Agent Torres", "shift_cost": 90, "shifts": 22},
    {"name": "Researcher Hall", "shift_cost": 150, "shifts": 10}
]

costs = list(map(lambda person: person["shift_cost"] * person["shifts"], staff_shifts))

print("Список общей стоимости:", costs)

max_cost = max(costs)

print("Максимальная стоимость:", max_cost)