# Write a function `five_multiples_of(n)` that prints the first five multiples of n.

def five_multiples_of(n):
    for i in range(1, 6):  # 1 through 5
        print(n * i)

# Test example
five_multiples_of(7)
# 7
# 14
# 21
# 28
# 35