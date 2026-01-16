# Write a function `num_odds(numbers)` that accepts a list of numbers.
# The function should return the count of odd numbers in the list.

def num_odds(numbers):
    count = 0
    for num in numbers:
        if num % 2 != 0:
            count += 1
    return count

# Test examples:
print(num_odds([4, 7, 2, 5, 9]))           # -> 3
print(num_odds([11, 31, 58, 99, 21, 60]))  # -> 4
print(num_odds([100, 40, 4]))              # -> 0
