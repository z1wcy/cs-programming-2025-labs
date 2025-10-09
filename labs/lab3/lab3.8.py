while True:
    num=input("Введите два числа через пробел или напиши \"стоп\":")
    if num =="стоп":
        break
    x, y= map(int, num.split())
    print(f'Сумма равна:{x+y}')
    print("")