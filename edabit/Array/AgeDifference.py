def age_difference(lst):
    lst = sorted(lst,reverse = True)
    print(lst)
    return lst[0] - lst[1]


print(age_difference([29, 1, 6, 8, 28])) # "1 year"

print(age_difference([43, 86, 49, 86]) )# "No age difference between spouses."

print(age_difference([2, 4, 6, 32, 27]) )# "5 years"