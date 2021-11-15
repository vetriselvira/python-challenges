def forbidden_letter(letter1,lst):
    for letter in lst:
        for let in letter:
            if letter1 in let:
                return False
    return True


print(forbidden_letter("r", ["rock", "paper", "scissors"])) # False

print(forbidden_letter("a", ["spoon", "fork", "knife"])) # True

print(forbidden_letter("m", [])) # True