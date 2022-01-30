# Caesar decoding

# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#     print("Welcome to Caesar cripting")
#     print("I hope u are all right")
#     print("bcs if not that means you are all left")
# greet()

# function that allows input

# def greet_with_name(name):
#     print(f"Hello, {name}! Welcome to Caesar cripting")
#     print(f"I hope u are all right,{name}")
#
# greet_with_name("Andrei")
#
# functions with more than one input
#
# def greet_with(name,location):
#     print(f"hello {name}")
#     print(f"what is it like in {location}")
#
# greet_with("andrei","piatra neamt")
#
# greet_with("piatra neamt","andrei")

# Functions with keyword arguments

# def greet_with(name,location):
#     print(f"hello {name}")
#     print(f"what is it like in {location}")
#
# greet_with(name="Andrei",location="Piatra Neamt")

# Ex 1 - wall painting
# import math
#
# def paint_calc(height, width, cover):
#     coverage = 5
#     area = height * width
#     number_of_cans = math.ceil(area/cover)
#     print(f"you'll need {number_of_cans} number of cans")
#
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# Verificarea unui numar daca este prim

# def prime_checker(number):
#     ok = 1
#     for n in range(2, number):
#         if number % n == 0:
#             ok = 0
#     if ok == 0:
#         print(f"number {number} in not prime")
#     else:
#         print(f"number {number} is prime")
#
#
# n = int(input("Check this number: "))
# prime_checker(number=n)