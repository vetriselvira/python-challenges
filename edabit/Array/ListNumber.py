def check(list1,num):
    for item in list1:
        if item == num:
            return True
    return False


print(check([1, 2, 3, 4, 5], 3) )# True

print(check([1, 1, 2, 1, 1], 3)) # False

print(check([5, 5, 5, 6], 5)) # True

print(check([], 5)) # False
