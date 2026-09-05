# Exercise 1. Arithmetic Product and Conditional Logic

# Practice Problem: Write a Python function that accepts two integer numbers.
# If the product of the two numbers is less than or equal to 1000,
# return their product;
# otherwise, return their sum


def productOfInts(a, b):
    if a * b < 1000:
        return a * b
    return a + b


print("Welcome to product and sum calculation")
prompt = True
while prompt:
    print("Enter 2 numbers separated by a space (e.g., 34 56):")
    intX, intY = map(int, input().split())

    print(productOfInts(intX, intY))
    print("Continue?")
    print("Y or N")

    # Correct ternary operator structure
    prompt = True if input().strip().upper() == "Y" else False
