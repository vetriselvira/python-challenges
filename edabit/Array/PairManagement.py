# packing
def make_pair(*num):
    return list(num)


print(make_pair(1, 2) )# [1, 2]

print(make_pair(51, 21)) # [51, 21]

print(make_pair(512124, 215)) # [512124, 215]

# unpacking


def fun(a, b, c, d):
    print(a, b, c, d)


# Driver Code
my_list = [1, 2, 3, 4]

# Unpacking list into four arguments
fun(*my_list)