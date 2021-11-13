def value_at(lst,div):
    return lst[int(div)]


print(value_at([1, 2, 3, 4, 5, 6], 10 // 2)) # 6

print(value_at([1, 2, 3, 4, 5, 6], 8.0 // 2) )# 5

print(value_at([1, 2, 3, 4], 6.535355314 // 2) )# 4

