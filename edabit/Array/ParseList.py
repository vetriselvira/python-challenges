def parse_list(lst):
    lst =[str(i) if type(i) == int else i for i in lst ]
    return lst


print(parse_list([1, 2, "a", "b"])) #  ["1", "2", "a", "b"]

print(parse_list(["abc", 123, "def", 456])) # ["abc", "123", "def", "456"]

print(parse_list([1, 2, 3, 17, 24, 3, "a", "123b"]) )# ["1", "2", "3", "17", "24", "3", "a", "123b"]

print(parse_list([])) # []