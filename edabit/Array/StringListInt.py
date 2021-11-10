def to_number_list(lst):
    for i in range(len(lst)):
        lst[i] = float(lst[i])
    return lst


print(to_number_list(["9.4", "4.2"]) )# [9.4, 4.2]

print(to_number_list(["99", "20"]) )# [99, 20]

print(to_number_list(["9.5", "8.8"])) # [9.5, 8.8]