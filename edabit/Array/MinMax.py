def max_and_min(list_of_nums):
    min_max = []
    small_num = list_of_nums[0]
    largest_num = list_of_nums[0]
    for item in range(len(list_of_nums)):
        if small_num > list_of_nums[item]:
            small_num = list_of_nums[item]
        elif largest_num < list_of_nums[item]:
            largest_num = list_of_nums[item]
    min_max.append(small_num)
    min_max.append(largest_num)
    return min_max


print(max_and_min([1, 2, 3, 4, 5]) ) # 2
# print('smallest num is :{}, largest num is :{}'.format({small},{large}))

print(max_and_min([2334454, 5])) # -345
# print('smallest num is :{}, largest num is :{}'.format({small},{large}))

print(max_and_min([-76, 1.345, 1, 0])) # -76
# print('smallest num is :{}, largest num is :{}'.format({small},{large}))

print(max_and_min([0.4356, 0.8795, 0.5435, -0.9999])) # -76
# print('smallest num is :{}, largest num is :{}'.format({small},{large}))
