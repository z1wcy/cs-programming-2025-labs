#task 8

purchase = float(input("Введите сумму покупки: "))

if purchase < 1000:
    discount = 0
elif purchase <= 5000:
    discount = 5
elif purchase <= 10000:
    discount = 10
else:
    discount = 15

sum = purchase * discount / 100
final = purchase - sum

print(f'Сумма покупки: {purchase} руб.')
print(f'Ваша скидка составила: {sum} руб.')
print(f'Итого к оплате: {final} руб.')