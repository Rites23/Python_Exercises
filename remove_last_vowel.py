# Write a function `remove_last_vowel` that accepts a string as an argument.
# The function should return the string with its last vowel removed.
# Vowels are the letters: a, e, i, o, u

def remove_last_vowel(text):
    vowels = "aeiou"

    for i in range(len(text) - 1, -1, -1):
        if text[i].lower() in vowels:
            return text[:i] + text[i+1:]

    return text

# Test examples:
print(remove_last_vowel("speaker"))   # 'speakr'
print(remove_last_vowel("trading"))   # 'tradng'
print(remove_last_vowel("thunder"))   # 'thundr'
print(remove_last_vowel("myth"))      # 'myth'