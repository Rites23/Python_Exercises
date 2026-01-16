# Write a function `alternating_caps(sentence)` that accepts a string containing a sentence.
# The function should return the sentence where words alternate between lowercase and uppercase.

def alternating_caps(sentence):
    words = sentence.split()
    result = []

    for i, word in enumerate(words):
        if i % 2 == 0:
            result.append(word.lower())
        else:
            result.append(word.upper())

    return ' '.join(result)

# Test examples: 
print(alternating_caps("take them to school"))           # -> 'take THEM to SCHOOL'
print(alternating_caps("What did ThEy EAT before?"))    # -> 'what DID they EAT before?'
