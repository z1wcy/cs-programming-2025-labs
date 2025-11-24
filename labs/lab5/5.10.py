x = [("Анна", [5, 4, 5]), ("Иван", [3, 4, 4]), ("Мария", [5, 5, 5])]
f = {}

for i in x:
   q,w = i
   f.update(q:sum(w)//len(w))
   
  

print()


print(f)