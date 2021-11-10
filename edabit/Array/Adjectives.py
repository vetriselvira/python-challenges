def adjectives_used(dict_of_adjectives):
    return len(dict_of_adjectives)


a = adjectives_used({"a": "moron"}) # 1
print(a)

b = adjectives_used({ "a": "idiot", "b": "idiot", "c": "idiot" }) # 3
print(b)

c = adjectives_used({ "a": "moron", "b": "scumbag", "c": "moron", "d": "dirtbag" }) # 4
print(c)