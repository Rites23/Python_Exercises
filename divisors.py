# Write a function `divisors(num)` that accepts a number.
# The function should return a list containing all positive numbers that divide num exactly.

def divisors(num):
    result = []
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)
    return result

# Test examples:
print(divisors(15))  # -> [1, 3, 5, 15]
print(divisors(7))   # -> [1, 7]
print(divisors(24))  # -> [1, 2, 3, 4, 6, 8, 12, 24]
