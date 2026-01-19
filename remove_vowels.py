# Write a function `remove_dupes(lst)` that accepts a list and returns a new list
# where each element appears only once.

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in s if char not in vowels)

# Test examples:
print(remove_vowels("jello"))        # 'jll'
print(remove_vowels("sensitivity"))  # 'snstvty'
print(remove_vowels("cellar door"))  # 'cllr dr'

