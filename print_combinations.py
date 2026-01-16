# Write a function `print_combinations(arr1, arr2)` that accepts two lists.
# The function should print all combinations taking one element from the first list
# and one from the second list. It doesn't need to return anything.

def print_combinations(arr1, arr2):
    for item1 in arr1:
        for item2 in arr2:
            print(f"{item1} {item2}")

# Test examples:
colors = ["gray", "cream", "cyan"]
clothes = ["shirt", "flannel"]

print_combinations(colors, clothes)
# prints:
# gray shirt
# gray flannel
# cream shirt
# cream flannel
# cyan shirt
# cyan flannel
