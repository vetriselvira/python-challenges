def birthday_cake_candles(list1):
    m = max(list1)
    return(list1.count(m))


print(birthday_cake_candles([4, 4, 1, 3])) # 2
# The maximum height candles are four units high.
# There are two of them, so you return 2.

print(birthday_cake_candles([3, 2, 1, 3])) # 2

print(birthday_cake_candles([82, 49, 82, 82, 41, 82, 15, 63, 38, 25])) # 4