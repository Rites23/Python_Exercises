# Write a function `total(numbers)` that accepts a list of numbers as an argument.
# The function should return the sum of all elements in the list.

def total(numbers):
    return sum(numbers)

# Test examples
print(total([3, 2, 8]))        # -> 13
print(total([-5, 7, 4, 6]))    # -> 12
print(total([7]))              # -> 7
print(total([]))               # -> 0