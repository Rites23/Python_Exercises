# Write a function `string_repeater(text, n)` that returns a new string
# consisting of `text` repeated `n` times.

def string_repeater(text, n):
    return text * n

# Test examples
print(string_repeater("q", 4))    # -> 'qqqq'
print(string_repeater("go", 2))   # -> 'gogo'
print(string_repeater("tac", 3))  # -> 'tactactac'
