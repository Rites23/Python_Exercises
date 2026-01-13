# Write a function `no_ohs(text)` that prints each character of the string except 'o'.

def no_ohs(text):
    for char in text:
        if char != 'o':  # skip 'o'
            print(char)

# Test example
no_ohs("code")
# c
# d
# e

