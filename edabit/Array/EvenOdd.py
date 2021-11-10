def even_or_odd(n):
    total = sum(n)
    if total % 2 == 0:
        return "even"
    else:
        return "odd"


print(even_or_odd([0])) # "even"

print(even_or_odd([1])) # "odd"

print(even_or_odd([])) # "even"

print(even_or_odd([0, 1, 5])) # "even"