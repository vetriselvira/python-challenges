def count_true(lst):
    return lst.count(True)


print(count_true([True, False, False, True, False]) )# 2

print(count_true([False, False, False, False])) # 0

print(count_true([])) # 0
