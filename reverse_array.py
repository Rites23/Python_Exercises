# Write a function `reverse_array(arr)` that accepts a list as an argument.
# The function should return a list containing the elements of the original list in reverse order.

def reverse_array(arr):
    return arr[::-1]

# Test examples:
print(reverse_array(["zero", "one", "two", "three"]))  # -> ['three', 'two', 'one', 'zero']
print(reverse_array([7, 1, 8]))  # -> [8, 1, 7]