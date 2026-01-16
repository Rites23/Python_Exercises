# Write a function `filter_long_words(words)` that accepts a list of strings.
# The function should return a new list containing only the words that have
# less than 5 characters.

def filter_long_words(words):
    return [word for word in words if len(word) < 5]

# Test examples:
print(filter_long_words(["kale", "cat", "retro", "axe", "heirloom"]))
# -> ['kale', 'cat', 'axe']

print(filter_long_words(["disrupt", "pour", "trade", "pic"]))
# -> ['pour', 'pic']
