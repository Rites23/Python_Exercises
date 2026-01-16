# Write a function `two_sum(numbers, target)` that accepts a list of numbers and a target number.
# The function should return True if there exists a pair of distinct elements in the list that sum to the target.
# Otherwise, return False.

def two_sum(numbers, target):
    seen = set()
    for num in numbers:
        if target - num in seen:
            return True
        seen.add(num)
    return False

# Test examples:
print(two_sum([2, 3, 5, 9], 7))  # -> True
print(two_sum([2, 3, 5, 9], 4))  # -> False
print(two_sum([6, 3, 4], 10))    # -> True
print(two_sum([6, 5, 1], 10))    # -> False
