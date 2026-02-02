# **Task:**

# Write a function `pick_primes` that accepts a list of numbers.

# The function should return a **new list** containing **only the prime numbers** from the original list.

# You may want to **reuse the `is_prime` function**.

def is_prime(n):
    
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def pick_primes(numbers):
   
    return [num for num in numbers if is_prime(num)]

# Test examples:
print(pick_primes([12, 3, 7, 18, 11]))  # [3, 7, 11]
print(pick_primes([17, 23, 9, 42]))     # [17, 23]
print(pick_primes([4, 2048, 100, 55]))  # []
