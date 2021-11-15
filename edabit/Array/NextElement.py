def next_element(lst):
   diff = lst[-1] - lst[-2]
   lst[-1] = lst[-1] + diff
   return lst[-1]


print(next_element([3, 5, 7, 9])) # 11

print(next_element([-5, -6, -7])) # -8

print(next_element([2, 2, 2, 2, 2])) # 2