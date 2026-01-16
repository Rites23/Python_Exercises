# Write a function `bleep_vowels(text)` that accepts a string and returns
# a new string where all vowels (a, e, i, o, u) are replaced with '*'.

def bleep_vowels(text):
    vowels = "aeiou"
    result = ""

    for char in text:
        if char.lower() in vowels:
            result += "*"
        else:
            result += char

    return result

# Test examples:
print(bleep_vowels("skateboard"))    # -> 'sk*t*b**rd'
print(bleep_vowels("slipper"))       # -> 'sl*pp*r'
print(bleep_vowels("range"))         # -> 'r*ng*'
print(bleep_vowels("brisk morning")) # -> 'br*sk m*rn*ng'
