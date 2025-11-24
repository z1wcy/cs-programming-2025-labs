q =["яблоко", "груша", "банан", "киви", "апельсин", "ананас"]

e = [i[0] for i in q]
e1 = []
for x in e:
    t = [i for i in q if i[0]==x]
    e1.append(t)

    
dict ={x1:x2 for x1 in e for x2 in e1}

print(dict)