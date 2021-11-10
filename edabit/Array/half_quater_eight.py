def half_quarter_eight(n):
    list1 = []
    list1.append(n/2)
    list1.append(n/4)
    list1.append(n/8)
    return list1


print(half_quarter_eight(6)) # [3, 1.5, 0.75]

print(half_quarter_eight(22)) # [11, 5.5, 2.75]

print(half_quarter_eight(25)) # [12.5, 6.25, 3.125]

