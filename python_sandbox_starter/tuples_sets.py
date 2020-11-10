# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

fruits = ("Apples", "Oranges", "Grapes")
# fruits2 = tuple(("Apples", "Oranges", "Grapes"))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create Set
fruits_set = {"Apples", "Oranges", "Mango"}

# Check if in set

print("Apples" in fruits_set)

# Add to set
fruits_set.add("Blueberry")

# Remove from set
fruits_set.remove("Apples")

print(fruits_set)
