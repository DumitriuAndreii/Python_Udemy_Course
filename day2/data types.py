# ex 1
# num_char = len(input("What's your name? "))
#
# new_num_char = str(num_char)
#
# print("your name has " + new_num_char + " letters")

# ex 2
# a = float (123)
# print(type(a))
# print(a + float("100.5"))

# EX 3 - suma a doua cifre a unui numar
# two_digit_number = input("Type a two digit number: ")
# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])
# print(first_digit + second_digit)

# EX 4 - BMI calculator
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
#
# bmi = weight/(height**2)
#
# print(type(bmi))
# print(bmi)

# EX 5

# print(8/3)
# print(int(8/3))
# print(round(8/3,2))

# Ex 6

# score = 4
# heigh = 1.8
# is_winning = True
# #f - string caracthers
#
# print(f"your score is {score} and your height is {heigh} and you are winning{is_winning}")

# Ex 6 - calculator pentru a afla cate zile mai am de trait daca mor la 90 de ani

# age = input("What is your current age?")
# int_age = int(age)
# years_remaining = 90 - int_age
# days = years_remaining * 365
# weeks = years_remaining * 52
# months = years_remaining * 12
#
# print(f"you have {days} days left, {weeks} weeks, and {months} months left ")

# FINAL TASK - TIP CALCULATOR

# print("Welcome to the tip calculator! ")
# bill = float(input("what was your total bill ? "))
# tip_percentage = float(input("what percentage tip would you like to give? 10, 12 or 15? "))
# nr_of_ppl = int(input("How many people to split the bill? "))
# result = round((((bill * tip_percentage/100) + bill )/nr_of_ppl),2)
# result = "{:.2f}".format(result)
# print(f"each person should pay {result} dollars")
