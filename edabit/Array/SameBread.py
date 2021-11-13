def has_same_bread(lst1,lst2):
    if lst1[0] == lst2[0] and lst1[-1] == lst2[-1]:
        return True
    else:
        return False


print(has_same_bread(
  ["white bread", "lettuce", "white bread"],
  ["white bread", "tomato", "white bread"]
) )# True

print(has_same_bread(
  ["brown bread", "chicken", "brown bread"],
  ["white bread", "chicken", "white bread"]
) )# False

print(has_same_bread(
  ["toast", "cheese", "toast"],
  ["toast", "cheese", "toast"]
)) # False
