# Write a function `remove_short_words(sentence)` that accepts a string containing a sentence.
# The function should return a new sentence where all words shorter than 4 characters are removed.

def remove_short_words(sentence):
    words = sentence.split()
    long_words = [word for word in words if len(word) >= 4]
    return ' '.join(long_words)

# Test examples:
print(remove_short_words("knock on the door will you"))  # -> 'knock door will'
print(remove_short_words("a terrible plan"))            # -> 'terrible plan'
print(remove_short_words("run faster that way"))        # -> 'faster that'
