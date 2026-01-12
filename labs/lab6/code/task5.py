s = input().strip()
cleaned = ''.join(c.lower() for c in s if c.isalnum())
print("Да" if cleaned == cleaned[::-1] else "Нет")