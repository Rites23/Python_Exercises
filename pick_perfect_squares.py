# Write a function `pick_perfect_squares` that accepts a list of numbers.
# The function should return a list containing only the perfect squares.
#
# A perfect square is a number that can be written as n * n.

def pick_perfect_squares(nums):
    result = []

    for num in nums:
        if num >= 0:
            root = int(num ** 0.5)
            if root * root == num:
                result.append(num)

    return result

# Test Examples:
print(pick_perfect_squares([6, 4, 81, 21, 36]))
# [4, 81, 36]

print(pick_perfect_squares([100, 24, 144]))
# [100, 144]

print(pick_perfect_squares([30, 25]))
# [25]