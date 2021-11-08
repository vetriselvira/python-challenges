def concat(list1,list2):
    for item in list2:
        list1.append(item)
    return list1


print(concat([1, 3, 5], [2, 6, 8])) # [1, 3, 5, 2, 6, 8]

print(concat([7, 8], [10, 9, 1, 1, 2])) # [7, 8, 10, 9, 1, 1, 2]

print(concat([4, 5, 1], [3, 3, 3, 3, 3])) # [4, 5, 1, 3, 3, 3, 3, 3]
