x= int(input("введите число от 1 до 9"))
if x>9 or x<1:
    print("плохо плохо")
else:
    for i in range(1,11):
        print(x*i)