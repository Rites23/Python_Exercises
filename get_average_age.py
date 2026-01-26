# Write a function `get_average_age` that accepts a **list of dictionaries**.

# Each dictionary represents a person and contains an `age` key.

# The function should return the **average age** of all people.

def get_average_age(people):
    total_age = sum(person["age"] for person in people)
    count = len(people)
    if count == 0:
        return 0  
    return round(total_age / count, 2)  

# Test examples:
peeps = [
    {"name": "Lovelace", "age": 36, "born": "London, UK"},
    {"name": "Kleene", "age": 85, "born": "Connecticut, US"},
    {"name": "Turing", "age": 41, "born": "London, UK"},
    {"name": "Hopper", "age": 85, "born": "New York, US"},
]

print(get_average_age(peeps))
# 61.75

people = [
    {"name": "Orwell", "age": 46, "born": "Bihar, India"},
    {"name": "Bradbury", "age": 91, "born": "California, US"},
    {"name": "Huxley", "age": 69, "born": "California, US"},
]

print(get_average_age(people))
# 68.67
