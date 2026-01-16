# Write a function `strings_to_lengths(strings)` that accepts a list of strings.
# The function should return a new list containing the lengths of each string.

def strings_to_lengths(strings):    
    lengths = []
    for string in strings:
        lengths.append(len(string))
    return lengths  

# Test examples:
print(strings_to_lengths(["belly", "echo", "irony", "pickled"]))   # -> [5, 4, 5, 7]
print(strings_to_lengths(["on", "off", "handmade"]))              # -> [2, 3, 8]
