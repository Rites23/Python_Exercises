# Write a function `most_letter_word(sentence, char)` that accepts:
# - a sentence string
# - a single character
#
# The function should return the word in the sentence that contains the
# character the greatest number of times.
#
# You can assume the sentence contains at least one word.
# If there is a tie, return the word that appears first in the sentence.

def most_letter_word(sentence, char):
    words = sentence.split()

    max_count = -1
    best_word = ""

    for word in words:
        count = word.count(char)

        if count > max_count:
            max_count = count
            best_word = word

    return best_word

# Test examples:
print(most_letter_word(
'she received an award for excellence in science','e'
))# 'excellence'

print(most_letter_word(
'she received an award for excellence in science','a'
))# 'award'

print(most_letter_word(
'I hope sophomore year comes soon','o'
))# 'sophomore'

