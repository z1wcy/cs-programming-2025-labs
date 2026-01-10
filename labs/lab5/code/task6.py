print("task_6")

list = [22, 'tv', 2.11, 'wow', True, 33, [1,2], None]
fool = dict()
for i in list:
    try:
        fool[i] = i
    except:
        pass
print(fool)