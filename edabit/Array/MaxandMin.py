def max_and_min(list_of_nums):
    small_num = list_of_nums[0]
    largest_num = list_of_nums[0]
    for item in range(len(list_of_nums)):
        if small_num > list_of_nums[item]:
            small_num = list_of_nums[item]
        elif largest_num < list_of_nums[item]:
            largest_num = list_of_nums[item]
    return small_num,largest_num


small,large = max_and_min([34, 15, 88, 2]) # 2
print('smallest num is :{}, largest num is :{}'.format({small},{large}))

small,large = max_and_min([34, -345, -1, 100]) # -345
print('smallest num is :{}, largest num is :{}'.format({small},{large}))

small = max_and_min([-76, 1.345, 1, 0]) # -76
print('smallest num is :{}, largest num is :{}'.format({small},{large}))

small = max_and_min([0.4356, 0.8795, 0.5435, -0.9999]) # -76
print('smallest num is :{}, largest num is :{}'.format({small},{large}))

