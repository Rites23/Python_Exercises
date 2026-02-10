# Write a function `lala_language` that accepts a sentence string as an argument.
# The function should return a new sentence where words longer than 3 characters
# are modified.
#
# Modified words should have each vowel followed by 'l' and the same vowel again.
# See the examples below.

def lala_language(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result_words = []

    for word in words:
        if len(word) <= 3:
            result_words.append(word)
        else:
            new_word = ""

            for ch in word:
                if ch in vowels:
                    new_word += ch + "l" + ch
                else:
                    new_word += ch

            result_words.append(new_word)

    return " ".join(result_words)

# Test Examples:
print(lala_language('this is pretty strange'))
# thilis is preletty stralangele

print(lala_language('can you speak our language'))
# can you spelealak our lalangulualagele