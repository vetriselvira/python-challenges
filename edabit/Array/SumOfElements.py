def get_sum_of_elements(list1):
    total = 0
    for item in list1:
        total = item + total
    return total


print(get_sum_of_elements([2, 7, 4])) # 13

print(get_sum_of_elements([45, 3, 0]) )# 48

print(get_sum_of_elements([-2, 84, 23])) # 105