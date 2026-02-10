# Write a function `censor_sentence(sentence, target_words)` that accepts:
# - a sentence string
# - a list of target words
#
# The function should return a new sentence where each target word
# is replaced with '*' characters of the same length.

def censor_sentence(sentence, target_words):
    words = sentence.split()
    result = []

    for word in words:
        if word in target_words:
            result.append("*" * len(word))
        else:
            result.append(word)

    return " ".join(result)

# Test Examples:
print(censor_sentence('where the heck is my celery', ['heck','celery']))
# 'where the **** is my ******'

print(censor_sentence('why you little sweetheart', ['sweetheart','salad']))
# 'why you little **********'