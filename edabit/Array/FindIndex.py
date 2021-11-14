def find_index(lst1,str1):
    return lst1.index(str1)


print(find_index(["hi", "edabit", "fgh", "abc"], "fgh") )# 2

print(find_index(["Red", "blue", "Blue", "Green"], "blue") )# 1

print(find_index(["a", "g", "y", "d"], "d")) # 3

print(find_index(["Pineapple", "Orange", "Grape", "Apple"], "Pineapple") )# 0