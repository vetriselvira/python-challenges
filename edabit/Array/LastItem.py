def last_ind(lst):
    if len(lst) == 0:
        return "None"
    else:
        return str(lst[-1])[-1]




print(last_ind([0, 4, 19, 34, 50, -9, 2])) # 2

print(last_ind("The quick brown fox jumped over the lazy dog"))# "g"

print(last_ind([])) # None