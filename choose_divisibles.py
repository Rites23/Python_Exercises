# Write a function `choose_divisibles(numbers, target)` that accepts a list of numbers and a target number.
# The function should return a new list containing only the elements divisible by the target.

def choose_divisibles(numbers, target):
    return [num for num in numbers if num % target == 0]

# Test examples: 
print(choose_divisibles([40, 7, 22, 20, 24], 4))  # -> [40, 20, 24]
print(choose_divisibles([9, 33, 8, 17], 3))       # -> [9, 33]
print(choose_divisibles([4, 25, 1000], 10))       # -> [1000]
