# Write a function `letter_map` that accepts:
# - a string
# - a dictionary
# The function should return a new string where characters that appear as keys in the dictionary
# are replaced with their corresponding values.

def letter_map(text, mapping):
    result = []
    for char in text:
        result.append(mapping.get(char, char))
    return "".join(result)

# Test examples: 
print(letter_map("symbolic", {"y": "i", "o": "a", "c": "k"}))
# 'simbalik'

