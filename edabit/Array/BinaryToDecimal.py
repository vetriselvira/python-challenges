def binary_to_decimal(lst):
    bin = ''.join(str(e) for e in lst)
    # print(bin)
    return int(bin,2)


print(binary_to_decimal([0, 0, 0, 1]) )# 1

print(binary_to_decimal([0, 0, 1, 0])) # 2

print(binary_to_decimal([1, 1, 1, 1, 1, 0, 1, 1, 0, 1]) )# 1005