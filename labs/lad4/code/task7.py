#task 7

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

if a <= b and a <= c:
    small = a
elif b <= a and b <= c:
    small = b
else :
    small = c

print(f'Наименьшее число: {small}')