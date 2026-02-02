# **Task:**

# Write a function `double_vowel` that accepts a string as an argument.

# The function should return a new string where **every vowel** in the original string is repeated **twice consecutively**.

# Vowels are: `a, e, i, o, u`

def double_vowel(text):
    vowels = "aeiou"
    result = ""

    for ch in text:
        if ch in vowels:
            result += ch * 2
        else:
            result += ch

    return result

# Test examples:
print(double_vowel("runner"))
# ruunneer

print(double_vowel("stoplight"))
# stoopliight

print(double_vowel("gardener"))
# gaardeeneer