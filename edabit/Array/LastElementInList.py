def get_last_value(number_list):
    return number_list[-1]


a = get_last_value([1, 2, 3])  # 1
print(a)

b = get_last_value(["cat", "dog", "duck"])  # 80
print(b)

c = get_last_value([True, False, True]) # -500
print(c)

d = get_last_value([7, "String", False]) # -500
print(d)