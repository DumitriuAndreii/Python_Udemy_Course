# EX1
# print("welcome to the rollercoaster!")
# height = int(input("what s your height in cm?"))
# if height >= 120:
#     print("you can ride the rollercoaster!")
# else:
#     print("sorry you are too small to ride it ")

#Ex 2 - verificarea numerelor par/impar
# number = int(input("Which number do you want to check? "))
# if number % 2 == 1:
#     print("This number is odd")
# else:
#     print("This number is even")

#Ex 3 -  nested if/else rollercoaster
# print("welcome to the rollercoaster!")
# height = int(input("what s your height in cm?  "))
#
# if height >= 120:
#     print("you can ride the rollercoaster!")
#     age = int(input("what's your age?  "))
#     if age <= 12:
#         print("Your ticket will be 5$")
#     elif age <=18:
#         print("Your ticket will be 7$")
#     else:
#         print("Your ticket will be 7$")
# else:
#     print("sorry you are too small to ride it ")

#Ex 4 - BMI calculator (upgraded)
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
#
# bmi = round(weight/(height**2))
#
# if bmi <= 18:
#     print(f"Your BMI is {bmi}, you are underweight")
# elif bmi <= 22:
#     print(f"Your BMI is {bmi}, you are normal weight")
# elif bmi <=28:
#     print(f"Your BMI is {bmi}, you are slightly overweight")
# elif bmi <=33:
#     print(f"Your BMI is {bmi}, you are obese")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese")

#Ex 5 - Leap year

# year = int(input("Which year do you want to check? "))
# ok = False
# if year % 4 == 0:
#     ok = True
# if year % 100 == 0:
#     ok = False
# if year % 400 == 0:
#     ok = True
# if ok:
#     print("this is a leap year")
# else:
#     print("this is not a leap year")

#V2 Ex5 - leap year

# year = int(input("Which year do you want to check? "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("This is a leap year")
#         else:
#             print("this is not a leap year")
#     else:
#         print("this is a leap year")
# else:
#     print("This is not a leap year")

#EX 6 - Rollercoaster upgraded
# print("welcome to the rollercoaster!")
# height = int(input("what s your height in cm?  "))
# bill = 0
#
# if height >= 120:
#     print("you can ride the rollercoaster!")
#     age = int(input("what's your age?  "))
#     if age <= 12:
#         bill = 5
#         print("child tickets are 5$")
#     elif age <=18:
#         bill = 7
#         print("youth tickets are 7$")
#     else:
#         bill = 12
#         print("adult tickets are 12$")
#
#     wants_photo = input("do you want a photo taken? Y or N ")
#     if wants_photo == "Y":
#         #add 3 $ to the bill
#         bill += 3
#     print(f"your bill will be {bill} dollars")
# else:
#     print("sorry you are too small to ride it ")

#Ex 7 - Pizza order

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# price = 0
# if size == "S":
#     price = 15
#     if add_pepperoni == "Y":
#         price += 2
# if size == "M":
#     price = 20
#     if add_pepperoni == "Y":
#         price += 3
# if size == "L":
#     price = 20
#     if add_pepperoni == "Y":
#         price += 3
# if extra_cheese == "Y":
#     price += 1
#
# print(f"Your total will be {price} dollars")

# EX 6 - Rollercoaster upgraded
# print("welcome to the rollercoaster!")
# height = int(input("what s your height in cm?  "))
# bill = 0
#
# if height >= 120:
#     print("you can ride the rollercoaster!")
#     age = int(input("what's your age?  "))
#     if age <= 12:
#         bill = 5
#         print("child tickets are 5$")
#     elif age <=18:
#         bill = 7
#         print("youth tickets are 7$")
#     elif age >=45 and age <=55 :
#         print("You just got a free ride")
#     else:
#         bill = 12
#         print("adult tickets are 12$")
#
#
#     wants_photo = input("do you want a photo taken? Y or N ")
#     if wants_photo == "Y":
#         #add 3 $ to the bill
#         bill += 3
#     print(f"your bill will be {bill} dollars")
# else:
#     print("sorry you are too small to ride it ")

#Ex 7 - Love calculator

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
#
# result = 0
# combined_names = name1.lower() + name2.lower()
# print(combined_names)
#
# t1 = combined_names.count('t')
# r1 = combined_names.count('r')
# u1 = combined_names.count('u')
# e1 = combined_names.count('e')
# l1 = combined_names.count('l')
# o1 = combined_names.count('o')
# v1 = combined_names.count('v')
#
# result = 10*t1 + 10*r1 + 10*u1 + 10*e1 + l1 + o1 + v1 + e1
# if result < 10 or result > 90:
#     print(f"Your score is {result}, you go together like coke and mentos")
# elif result >=40 and result <=50:
#     print(f"Your score is {result}, you are alright together.")
# else:
#     print(f"Your score is {result}")


#DAY 3 FINAL PROJECT
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
# step1 = input(("You are at a cross road. Where do u wnat to go 'left' or 'right'? "))
# if step1 == 'left':
#     step2 = input("You arrived near a lake. Do you want to swim or to wait? 'swim' or 'wait'")
#     if step2 == 'wait':
#         step3 = input("you saw a random house nearby with 3 doors. do you open the 'red' the 'blue' or the yellow'?  ")
#         if step3 == 'yellow':
#             print("You win!")
#         else:
#             print("You got into a room full of snakes! Game over! ")
#     else:
#         print("you got eaten by sharks! Game over! ")
# else:
#     print("you took the wrong path! game over! ")






