# **Task:**

# Write a function `is_prime` that accepts a number as an argument.

# The function should return `True` if the number is prime, otherwise return `False`.

# A prime number:

# - Is greater than 1
# - Is divisible only by 1 and itself

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

# Test examples:
print(is_prime(11))# True
print(is_prime(8))# False
print(is_prime(7))# True
print(is_prime(21))# False
print(is_prime(2))# True
print(is_prime(15))# False
print(is_prime(1))# False