def primes(a,b):
    primes_list = []
    for num in range(max(2, a), b + 1):
        if num > 1:
            for i in range (2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes_list.append(num)

    return primes_list if primes_list else "Error!"

a = int(input("Начало диапазона:"))
b = int(input("Конец диапазона:"))
print(primes(a, b))

primes(a,b)