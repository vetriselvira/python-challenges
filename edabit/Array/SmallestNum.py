def smallest_num(list_of_nums):
    small_num = list_of_nums[0]
    for item in range(len(list_of_nums)):
        if small_num > list_of_nums[item]:
            small_num = list_of_nums[item]
    return small_num


small = smallest_num([34, 15, 88, 2]) # 2
print(small)

small = smallest_num([34, -345, -1, 100]) # -345
print(small)

small = smallest_num([-76, 1.345, 1, 0]) # -76
print(small)

small = smallest_num([0.4356, 0.8795, 0.5435, -0.9999]) # -76
print(small)

small = smallest_num([7, 7, 7] ) # -76
print(small)
