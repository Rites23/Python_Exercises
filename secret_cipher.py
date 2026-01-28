# **Task:**

# Write a function `secret_cipher` that accepts:

# - a string
# - a dictionary (cipher map)

# Rules:

#- Replace each character in the string with its corresponding value from the dictionary
# - If a character does **not** exist as a key in the dictionary, replace it with `"?"`
# - Return the resulting string

def secret_cipher(text, cipher):
    result = ""

    for char in text:
        result += cipher.get(char, "?")

    return result

# Test examples:
print(secret_cipher("jello", {"j":"r","l":"s","e":"i" }))
# 'riss?'

print(secret_cipher("lantern", {"e":"o","l":"p","n":"m","r":"j" }))
# 'p?m?ojm'
