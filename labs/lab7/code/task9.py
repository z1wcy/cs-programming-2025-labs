shifts = [6, 12, 8, 24, 10, 4]

valid_shifts = list(filter(lambda x: 8 <= x <= 12, shifts))

print("Смены охраны, которые длятся от 8 до 12 часов включительно: ")
print(valid_shifts)