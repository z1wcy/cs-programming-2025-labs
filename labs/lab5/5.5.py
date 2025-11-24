product = {'яблоко': 130, 
           'груша': 100, 
           "банан": 37, 
           "пипидастр": 2000
}

print(min(product, key=product.get))
print(max(product, key=product.get))


