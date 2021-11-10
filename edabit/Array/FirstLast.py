def first_last(n):
    # fl = []
    # fl.append(n[0])
    # fl.append(n[-1])
    # return fl
    return [n.pop(0),n.pop()]



print(first_last([5, 10, 15, 20, 25]))  # [5, 25]

print(first_last(["edabit", 13, None, False, True]))  # ["edabit", True]

print(first_last([None, 4, "6", "hello", None])) # [None, None]