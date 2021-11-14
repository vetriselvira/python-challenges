def find_the_falsehoods(lst):
    f = [0,None,[],'']
    i = [i for i in lst if i in f]
    return i


print(find_the_falsehoods([0, 1, 2, 3])) # [0]

print(find_the_falsehoods(["", "a", "ab"])) # [""]

print(find_the_falsehoods([None, 1, [], [0], 0])) # [None, [], 0]

print(find_the_falsehoods([])) # []

print(find_the_falsehoods([[]])) # [[]]

print(find_the_falsehoods([[[]]]) )# []