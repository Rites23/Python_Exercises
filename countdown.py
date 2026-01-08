# Write `countdown(start)` that prints from start down to 1.

def countdown(start):
    for i in range(start, 0, -1):  # start, stop (exclusive), step -1
        print(i)

# Test
countdown(5)
# 5
# 4
# 3
# 2
# 1
