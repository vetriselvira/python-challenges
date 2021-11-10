def all_truthy(*n):
    for i in n:
        if i == False or i == 0:
            return False
    return True


print(all_truthy(True, True, True)) # True

print(all_truthy(True, False, True) )# False

print(all_truthy(5, 4, 3, 2, 1, 0)) # False