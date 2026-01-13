# Write a function `product_up_to(max_num)` that returns the product of all numbers
# from 1 to max_num inclusive.

def product_up_to(max_num):
    product = 1
    for i in range(1, max_num + 1):
        product *= i
    return product

# Test examples
print(product_up_to(4))  # -> 24   
print(product_up_to(5))  # -> 120  
print(product_up_to(7))  # -> 5040 