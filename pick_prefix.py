# Write a function `pick_prefix(strings, prefix)` that accepts:
# - a list of strings
# - a prefix string
#
# The function should return a list of words that begin with the prefix.

def pick_prefix(strings, prefix):
    return [word for word in strings if word.startswith(prefix)]

# Test examples:
print(pick_prefix(['connect','company','concert','cram'],'con'))
# ['connect', 'concert']

print(pick_prefix(['miner','mistake','misspeak','moose','mission'],'mis'))
# ['mistake', 'misspeak', 'mission']