# Write a function that prints the multiplication table of a number up to 10.

def multiplication_table(num):
    for i in range(1, 11):  
        print(num * i)

# Test example
multiplication_table(4)
# 4
# 8
# 12
# ...
# 40
