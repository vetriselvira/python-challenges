def rotate_by_one(lst):
    lst = lst[-1:] + lst[ :-1]
    return lst


print(rotate_by_one([1, 2, 3, 4, 5])) # [5, 1, 2, 3, 4]

print(rotate_by_one([6, 5, 8, 9, 7])) # [7, 6, 5, 8, 9]

print(rotate_by_one([20, 15, 26, 8, 4])) # [4, 20, 15, 26, 8]