# Write a function `sum_of_range(n)` that prints the sum of numbers from 1 to n.

def sum_of_range(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print(total)

# Test examples
sum_of_range(5)   # prints: 15
sum_of_range(10)  # prints: 55
