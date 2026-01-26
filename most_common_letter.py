# Write a function `most_common_letter` that accepts a string as an argument.

# The function should return the character that appears **most frequently** in the string.

# You may assume:

# - There are **no ties**
# - The string contains only lowercase letters

def most_common_letter(text):
    counts = {}

    for char in text:
        counts[char] = counts.get(char, 0) + 1

    most_common = max(counts, key=counts.get)

    return most_common


# Test examples:
print(most_common_letter("building"))
# 'i'

print(most_common_letter("shoestring"))
# 's'

print(most_common_letter("preparedness"))
# 'e'
