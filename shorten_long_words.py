# Write a function `shorten_long_words(sentence)` that accepts a string and returns
# the same sentence where words longer than 4 characters have their vowels removed.

def shorten_long_words(sentence):
    vowels = "aeiouAEIOU"
    words = sentence.split()
    result = []

    for word in words:
        if len(word) > 4:
            shortened = ""
            for char in word:
                if char not in vowels:
                    shortened += char
            result.append(shortened)
        else:
            result.append(word)

    return " ".join(result)

# Test examples:
print(shorten_long_words("they are very noble people"))  # 'they are very nbl ppl'
print(shorten_long_words("stick with it"))  # 'stck with it'
print(shorten_long_words("ballerina, you must have seen her"))  # 'bllrna, you must have seen her'