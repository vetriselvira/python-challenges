def back_to_home(lst):
    n = lst.count('N')
    e = lst.count('E')
    w = lst.count('W')
    s = lst.count('S')
    if n == s and e == w:
        return True
    else:
        return False


print(back_to_home("EEWEWW") )# False

print(back_to_home("NENESSWW")) # True

print(back_to_home("NEESSW")) # False
