dict = {
    'hello': 'привет',
    'world': 'мир',
    'house': 'дом',
    'cat': 'кот',
    'dog': 'собака',
    'book': 'книга'
    
}
x = input("Веди русское слово:")

for i,w in dict.items():
    if x == w:
        print(i)
        break
    


