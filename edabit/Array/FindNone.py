def find_none(lst):
    idx = [i for i in range(len(lst)) if lst[i] is None]
    if len(idx) > 0:
        return idx[0]
    else:
        return -1


print(find_none([1, 2, None])) # 2

print(find_none([None, 1, 2, 3, 4]))# 0

print(find_none([0, 1, 2, 3, 4])) # -1