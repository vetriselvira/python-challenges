from functools import reduce


def find_difference(lst1,lst2):
    x = reduce((lambda x, y: x*y),lst1)
    y = reduce((lambda x, y: x*y),lst2)
    return x - y


print(find_difference([ 28, 16, 29 ], [ 7, 8, 17 ]))# 12040

print(find_difference([ 9, 22, 18 ], [ 16, 24, 10 ]) )# 276

print(find_difference([ 1, 9, 25 ], [ 10, 7, 9 ])) # 405

print(find_difference([ 7, 6, 16 ], [ 26, 9, 26 ])) # 5412

