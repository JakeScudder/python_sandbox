# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create dict

person = {
    "first_name": "Jake",
    "last_name": "Morris",
    "age": 31
}

# Get Value
# print(person["first_name"])
# print(person.get("last_name"))

# Add key/value
person["phone"] = "555-5555"

# get dict keys
# print(person.keys())

# get dict items
# print(person.items())

# Copy dict
# person2 = person.copy()
# person2["city"] = "Boston"

# print(person2)

# Remove an item
del(person["age"])
person.pop("phone")

# Clear
# person.clear()

# # Length
# print(len(person))

# print(person)

# List of dict
people = [
    {"name": "Martha", "age": 25},
    {"name": "John", "age": 77}
]

print(people[0])
