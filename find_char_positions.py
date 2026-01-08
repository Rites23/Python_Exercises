# Write a function that prints all indexes where a character appears in a string.

def find_char_positions(text, char):
    for index in range(len(text)):
        if text[index] == char:
            print(index)

# Test example
find_char_positions("banana", "a")
# 1
# 3
# 5