def max_and_min(list_of_nums):
    small_num = list_of_nums[0]
    largest_num = list_of_nums[0]
    for item in range(len(list_of_nums)):
        if small_num > list_of_nums[item]:
            small_num = list_of_nums[item]
        elif largest_num < list_of_nums[item]:
            largest_num = list_of_nums[item]
    return largest_num - small_num


diff = max_and_min([34, 15, 88, 2]) # 2
print('Diff between largest and smallest num is:{}'.format(diff))

diff = max_and_min([34, -345, -1, 100]) # -345
print('Diff between largest and smallest num is:{}'.format(diff))

diff = max_and_min([-76, 1.345, 1, 0]) # -76
print('Diff between largest and smallest num is:{}'.format(diff))

diff = max_and_min([-3, 4, -9, -1, -2, 15]) # -76
print('Diff between largest and smallest num is:{}'.format(diff))