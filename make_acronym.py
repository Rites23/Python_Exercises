# Write a function `make_acronym(sentence)` that accepts a string containing a sentence.
# The function should return a string containing the first character of each word in the sentence.

def make_acronym(sentence):
    words = sentence.split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym

# Test examples: 
print(make_acronym("New York"))                 # -> 'NY'
print(make_acronym("same stuff different day")) # -> 'SSDD'
print(make_acronym("Laugh out loud"))           # -> 'LOL'
print(make_acronym("don't over think stuff"))   # -> 'DOTS'
