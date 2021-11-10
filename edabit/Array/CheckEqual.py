def check_equals(list1,list2):
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False


print(check_equals([1, 2], [1, 3])) # False

print(check_equals([1, 2], [1, 2])) # True

print(check_equals([4, 5, 6], [4, 5, 6]) )# True

print(check_equals([4, 7, 6], [4, 5, 6]) )# False

print(check_equals([1, 12], [11, 2])) # False