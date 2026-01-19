# Write a function `two_sum_pairs(numbers, target)` that returns all unique pairs from
# numbers that sum to target.

def two_sum_pairs(numbers, target):
    pairs = []
    seen = set()
    
    for num in numbers:
        complement = target - num
        if complement in seen:
            pairs.append([complement, num])
        seen.add(num)
    
    return pairs

# Test examples:
print(two_sum_pairs([2, 3, 4, 6, 5], 8))  # [[2, 6], [3, 5]]
print(two_sum_pairs([10, 7, 4, 5, 2], 12))  # [[10, 2], [7, 5]]
print(two_sum_pairs([3, 9, 8], 11))  # [[3, 8]]
print(two_sum_pairs([3, 9, 8], 10))  # []