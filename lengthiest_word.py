# Write a function `lengthiest_word(sentence)` that accepts a string containing a sentence.
# The function should return the longest word in the sentence.
# If there is a tie, return the word that appears later in the sentence.

def lengthiest_word(sentence):
    words = sentence.split()
    if not words:
        return None  
    
    longest = words[0]
    for word in words[1:]:
        if len(word) >= len(longest):  
            longest = word
    return longest

# Test examples:
print(lengthiest_word("I am pretty hungry"))                     # -> 'hungry'
print(lengthiest_word("we should think outside of the box"))    # -> 'outside'
print(lengthiest_word("down the rabbit hole"))                  # -> 'rabbit'
print(lengthiest_word("simmer down"))                            # -> 'simmer'

