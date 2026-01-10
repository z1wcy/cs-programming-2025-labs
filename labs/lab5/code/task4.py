print("task_4")

def sort_tuple(t):

    numbers = [x for x in t if isinstance(x, (int, float))]
    return tuple(sorted(numbers))


x = [9, 0.66, "indifference", "apps", 99, 14, None, 'True']
result = sort_tuple(tuple(x))
print(result)  