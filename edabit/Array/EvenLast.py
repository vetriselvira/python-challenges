def even_last(lst):
    i = [lst[i] for i in range(len(lst)) if i % 2 == 0]
    if len(lst) > 0:
        return sum(i) * lst[-1]
    else:
        return 0


print(even_last([])) # 0

print(even_last([1, 3, 3, 1, 10])) # 140

print(even_last([-11, 3, 3, 1, 10])) # 20