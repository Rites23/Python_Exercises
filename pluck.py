# Task:
# Write a function `pluck` that accepts:
# - a dictionary
# - a list of strings
#
# The function should return a new dictionary containing only
# the key–value pairs where:
# - the key exists in the provided list

def pluck(dictionary, keys):
    result = {}

    for key in keys:
        if key in dictionary:
            result[key] = dictionary[key]

    return result

# Test examples:
print(pluck(
    {"name": "Fido", "color": "Brown", "breed": "German Shepherd"},
    ["name", "breed"]
))
# { "name": "Fido", "breed": "German Shepherd" }

print(pluck(
    {"make": "Tesla", "mpg": 93, "model": "Model X", "color": "white"},
    ["make", "model"]
))
# { "make": "Tesla", "model": "Model X" }

