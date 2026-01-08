# Write a function `min_to_max(min_num, max_num)` that prints all numbers from min to max inclusive.

def min_to_max(min_num, max_num):
    for i in range(min_num, max_num + 1):
        print(i)

min_to_max(5, 9)
min_to_max(11, 13)
min_to_max(20, 11)   # what happens here?

# NOTE:
# range(20, 11 + 1) becomes range(20, 12)
# range() counts upwards by default (+1 step).
# Since 20 is already greater than 12, there are no values to loop through.
# Result: the loop never runs, so nothing is printed.
