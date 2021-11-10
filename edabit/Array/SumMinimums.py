def sum_minimums(n):
    min_items = []
    for items in n:
        min_items.append(min(items))
    return sum(min_items)

print(sum_minimums([
  [1, 2, 3, 4, 5],
  [5, 6, 7, 8, 9],
  [20, 21, 34, 56, 100]
] )) # 26