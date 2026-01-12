scp_objects = [
    {"scp": "SCP-096", "class": "Euclid"},
    {"scp": "SCP-173", "class": "Euclid"},
    {"scp": "SCP-055", "class": "Keter"},
    {"scp": "SCP-999", "class": "Safe"},
    {"scp": "SCP-3001", "class": "Keter"}
]

enhanced_security_scps = list(filter(lambda obj: obj["class"] != "Safe", scp_objects))

print("Список SCP-объектов, которые требуют усиленных мер содержания: ")
print(enhanced_security_scps)