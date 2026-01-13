# Write a function `odd_sum(max_num)` that returns the sum of all odd numbers
# from 1 to max_num inclusive.

def odd_sum(max_num):
    total = 0
    for i in range(1, max_num + 1, 2):  
        total += i
    return total

# Test examples
print(odd_sum(10))  # -> 25  # 1 + 3 + 5 + 7 + 9
print(odd_sum(5))   # -> 9   # 1 + 3 + 5
