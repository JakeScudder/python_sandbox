# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create Function
def sayHello(name="Sam"):
    return f"Hello {name}"


# print(sayHello("Jake"))

# Return values


def getSum(num1, num2):
    total = num1 + num2
    return total


sum = getSum(8, 9)
print(sum)


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions
