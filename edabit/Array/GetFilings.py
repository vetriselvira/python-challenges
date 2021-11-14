def get_fillings(lst):
    return lst[1:-1]


print(get_fillings(["bread", "ham", "cheese", "ham", "bread"])) # ["ham", "cheese", "ham"]

print(get_fillings(["bread", "sausage", "tomato", "bread"])) # ["sausage", "tomato"]

print(get_fillings(["bread", "lettuce", "bacon", "tomato", "bread"]) )# ["lettuce", "bacon", "tomato"]