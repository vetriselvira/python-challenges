def can_nest(lst1,lst2):
    lst1.sort()
    lst2.sort()
    if lst1[0] > lst2[0] and lst1[-1] < lst2[-1]:
        return "True"
    else:
        return "False"


print(can_nest([1, 2, 3, 4], [0, 6])) # True

print(can_nest([3, 1], [4, 0])) # True

print(can_nest([9, 9, 8], [8, 9]) )# False

print(can_nest([1, 2, 3, 4], [2, 3])) # False