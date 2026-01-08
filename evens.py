# Write a function `evens(max_num)` that prints all positive even numbers LESS than max_num.

def evens(max_num):
    for i in range(2, max_num, 2):  # start at 2, step by 2
        print(i)

evens(11)
evens(8)