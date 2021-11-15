def skip_the_sugar(lst):
    lst1 = ['Cola','Fanta']
    lst1 = [i.lower() for i in lst1]
    lst = [i for i in lst if i not in lst1]
    return lst


print(skip_the_sugar(["fanta", "cola", "water"])) # ["water"]

print(skip_the_sugar(["fanta", "cola"])) # []

print(skip_the_sugar(["lemonade", "beer", "water"])) # ["lemonade", "beer", "water"]