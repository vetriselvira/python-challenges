def sum_five(n):
    total = 0
    for item in n:
        if item > 5:
            total += item
    return total


print(sum_five([1, 5, 20, 30, 4, 9, 18])) # 77

print(sum_five([1, 2, 3, 4]))# 0

print(sum_five([10, 12, 28, 47, 55, 100]) )# 252