import time


a = time.time()

input()
print(a)

input()
b = time.time()
print(b)


time_lapsed = b - a

print(time_lapsed / 60)