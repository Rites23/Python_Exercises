# Write a function `div_by_either(num1, num2, max_num)` that prints all positive numbers
# less than max_num divisible by num1 or num2.

def div_by_either(num1, num2, max_num):
    for i in range(1, max_num):  # numbers from 1 up to max_num - 1
        if i % num1 == 0 or i % num2 == 0:
            print(i)

# Test example
div_by_either(4, 3, 16)
# 3
# 4
# 6
# 8
# 9
# 12
# 15