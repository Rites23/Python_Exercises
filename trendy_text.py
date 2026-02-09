# Write a function `trendy_text` that accepts a sentence string as an argument.
# The function should return the sentence where the last vowel of every word
# is removed.

def trendy_text(sentence):
    vowels = "aeiou"

    def remove_last_vowel(word):
        for i in range(len(word) - 1, -1, -1):
            if word[i].lower() in vowels:
                return word[:i] + word[i + 1:]
        return word

    words = sentence.split()

    result = []
    for word in words:
        result.append(remove_last_vowel(word))

    return " ".join(result)

# Test examples:
print(trendy_text("the concert will be epic"))
# 'th concrt wll be epc'

print(trendy_text("breakfast food is wonderful"))
# 'breakfst fod s wonderfl'

print(trendy_text("the weather will improve hopefully"))
# 'th weathr wll improv hopeflly'