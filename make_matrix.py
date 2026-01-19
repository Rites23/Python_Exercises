# Write a function `make_matrix(m, n, value)` that returns a 2D list of m rows and n columns
# filled with `value`.

def make_matrix(m, n, value):
    return [[value for _ in range(n)] for _ in range(m)]

# Test examples:
print(make_matrix(3, 5, None))
# Output:
# [
#  [None, None, None, None, None],
#  [None, None, None, None, None],
#  [None, None, None, None, None]
# ]

print(make_matrix(4, 2, "x"))
# Output:
# [
#  ['x', 'x'],
#  ['x', 'x'],
#  ['x', 'x'],
#  ['x', 'x']
# ]

print(make_matrix(2, 2, 0))
# Output:
# [
#  [0, 0],
#  [0, 0]
# ]