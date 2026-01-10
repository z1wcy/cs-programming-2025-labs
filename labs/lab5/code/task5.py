print("task_5")

def help(products):
    min1=min(products, key=products.get)
    max1=max(products, key=products.get)
    return min1, max1
products={"milk":120,"bread":50,"pie":220,"beer":90, "eggs":150}
print(help(products))