x=int(input("вводи число"))
if x <0:
    print("ок")
else:
    fac=1
    for i in range(1,x+1):
        fac*=i
print(fac)