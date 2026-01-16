# Write a function `number_range(min_val, max_val, step)` that accepts three numbers as arguments.
# The function should return a list of numbers starting from min_val to max_val (inclusive),
# incremented by step.

def number_range(min_val, max_val, step):
    result = []
    current = min_val
    while current <= max_val:
        result.append(current)
        current += step
    return result
 
# Test examples;
print(number_range(10, 40, 5))  # -> [10, 15, 20, 25, 30, 35, 40]
print(number_range(14, 24, 3))  # -> [14, 17, 20, 23]
print(number_range(8, 35, 6))   # -> [8, 14, 20, 26, 32]
