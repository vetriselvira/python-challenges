def largest_num(list_of_nums):
    big_num = 0
    for item in range(len(list_of_nums)):
        if big_num < list_of_nums[item]:
            big_num = list_of_nums[item]
    return big_num


big = largest_num([4, 5, 1, 3]) # 5
print(big)

big = largest_num([300, 200, 600, 150]) # 600
print(big)

big = largest_num([1000, 1001, 857, 1]) # 1001
print(big)