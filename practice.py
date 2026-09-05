# Exercise 1. Arithmetic Product and Conditional Logic

# Practice Problem: Write a Python function that accepts two integer numbers.
# If the product of the two numbers is less than or equal to 1000,
# return their product;
# otherwise, return their sum


# def productOfInts(a, b):
#     if a * b < 1000:
#         return a * b
#     return a + b


# print("Welcome to product and sum calculation")
# prompt = True
# while prompt:
#     print("Enter 2 numbers separated by a space (e.g., 34 56):")
#     intX, intY = map(int, input().split())

#     print(productOfInts(intX, intY))
#     print("Continue?")
#     print("Y or N")

#     # Correct ternary operator structure
#     prompt = True if input().strip().upper() == "Y" else False

# Exercise 2. Cumulative Sum of a Range

# Practice Problem: Iterate through the first 10 numbers (0–9).
# In each iteration, print the current number, the previous number,
# and their sum.

# for i in range(0, 10):
#     prev_num = 0 if i == 0 else i - 1
#     print(f"Previous number {prev_num}, Current number {i}, Sum {i + prev_num}")

# Exercise 3. String Indexing and Even Slicing

# Practice Problem: Display only those characters which are present at an even index number in given string.

# way 1
# str_even = input()

# for i in range(0, len(str_even)):
#     if i % 2 == 0:
#         print(str_even[i])

# # way 2

# word = "pynative"
# print("Original String is ", word)

# # Method: Using list slicing
# # format: [start:stop:step]
# even_chars = word[0::2]

# print("Printing only even index chars")
# for char in even_chars:
#     print(char)

