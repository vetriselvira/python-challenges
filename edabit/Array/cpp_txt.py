def cpp_txt(lst):
    lst.pop()
    lst = ''.join(lst)
    return lst


print(cpp_txt(["H", "i", "!", "\0"])) # "Hi!"

print(cpp_txt(["H", "e", "l", "l", "o", "!", "\0"]))  # "Hello!"

print(cpp_txt(["J", "A", "V", "a", "\0"]))# "JAVa"