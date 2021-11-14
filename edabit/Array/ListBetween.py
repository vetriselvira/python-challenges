def list_between(num1,num2,lst):
    lst = [i for i in lst if i > num1 and i < num2]
    return lst


print(list_between(3, 8, [1, 5, 95, 0, 4, 7])) # [5, 4, 7]

print(list_between(1, 10, [1, 10, 25, 8, 11, 6]) )# [8, 6]

print(list_between(7, 32, [1, 2, 3, 78])) # []