# Write a function `word_count(sentence, target_words)` that accepts a sentence string and a list of target words.
# The function should return a count of how many words in the sentence are also in target_words.

def word_count(sentence, target_words):
    words = sentence.split()  
    count = 0
    for word in words:
        if word in target_words:
            count += 1
    return count

print(word_count("open the window please", ["please", "open", "sorry"]))  # -> 2
print(word_count("drive to the cinema", ["the", "driver"]))               # -> 1
print(word_count("can I have that can", ["can", "I"]))                     # -> 3
