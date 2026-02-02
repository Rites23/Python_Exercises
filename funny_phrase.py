# **Task:**

# Write a function `funny_phrase` that accepts a sentence string.

# The function should return the sentence where **every other word** has its vowels repeated **twice consecutively**.

# Vowels are: `a, e, i, o, u`

def funny_phrase(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result = []

    for i, word in enumerate(words):
        # every other word (2nd, 4th, 6th, ...)
        if i % 2 == 1:
            new_word = ""
            for ch in word:
                if ch in vowels:
                    new_word += ch * 2
                else:
                    new_word += ch
            result.append(new_word)
        else:
            result.append(word)

    return " ".join(result)

# Test examples:
print(funny_phrase("she dreamed of being a runner"))
# she dreeaameed of beeiing a ruunneer

print(funny_phrase("park near the stoplight"))
# park neeaar the stoopliight

print(funny_phrase("we need many gardeners"))
# we neeeed many gaardeeneers