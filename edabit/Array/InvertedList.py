def invert_list(lst):
    return [-i for i in lst]


print(invert_list([1, 2, 3, 4, 5])) # [-1, -2, -3, -4, -5]

print(invert_list([1, -2, 3, -4, 5])) # [-1, 2, -3, 4, -5]

print(invert_list([])) # []