# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ["Apples", "Oranges", "Grapes", "Pears"]

# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))

# Get a value
# print(fruits[0])

# Get length
print(len(fruits))

# Append to list
fruits.append("Mangos")

# Remove from list
fruits.remove("Grapes")

# Insert into postion
fruits.insert(2, "Strawberries")

# Change value
fruits[0] = "Blueberries"

# Remove from position
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort Alphabetically

fruits.sort()

# Reverse Sort
fruits.sort(reverse=True)


print(fruits)
