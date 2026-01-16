# Write a function `your_average_function(numbers)` that accepts a list of numbers.
# The function should return the average of all elements in the list.
# If the list is empty, the function should return None.

def your_average_function(numbers):
    if not numbers:  
        return None
    return sum(numbers) / len(numbers)

# Test examples:
print(your_average_function([5, 2, 7, 24]))          # -> 9.5
print(your_average_function([100, 6]))               # -> 53.0
print(your_average_function([31, 32, 40, 12, 33]))   # -> 29.6
print(your_average_function([]))                     # -> None


