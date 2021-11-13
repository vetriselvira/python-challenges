def clean_up_list(lst):
    lst = [int(i) for i in lst]
    lst = [[i for i in lst if i % 2 == 0], [i for i in lst if i % 2 != 0]]
    return lst



print(clean_up_list(["8"]))  # [[8], []]

print(clean_up_list(["11"])) # [[], [11]]

print(clean_up_list(["7", "4", "8"])) # [[4, 8], [7]]

print(clean_up_list(["9", "4", "5", "8"])) # [[4, 8], [9, 5]]