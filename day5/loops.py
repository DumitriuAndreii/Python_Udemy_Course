#Ex 1 - for loop
# fruits = ["Apple", "Peach","Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print(fruits)

#Ex2 - average heighs
# student_heights = input("Input a list of student heights ").split()
#
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# total_height = 0
# for height in student_heights:
#     total_height = total_height + height
# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
#
# average_height = round(total_height/number_of_students)
# print(average_height)

#Ex 3 - highest score

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score in the class is: {highest_score}")

#Ex 4 - Loop with range function

# total= 0
# for number in range(1,101):
#     total+=number
# print(total)

# total_of_even = 0
# for number in range(2,101,2):
#     total_of_even += number
# print(total_of_even)

# FFFF IMPORTANT !! INTERVIEW
#Ex 5 - FIZZ BUZZ GAME
# for number in range(1,101):
#     if number % (3*5) == 0:
#         print("FIZZBUZZ")
#     elif number % 3 == 0:
#         print("FIZZ")
#     elif number % 5 == 0:
#         print("BUZZ")
#     else:
#         print(number)

#Ex 6 - FINAL PROJECT - PASSWORD GENERATOR
# import random
#
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy level
# password = ''
# for char in range(1,nr_letters+1):
#     password += random.choice(letters)
# for symb in range(1,nr_symbols+1):
#     password += random.choice(symbols)
# for number in range(1,nr_numbers+1):
#     password += random.choice(numbers)
# print(password)

#Hard lever

# # creem o lista pentru a o putea prelucra f usor
# password_list = []
# #adaugam numarul de litere dorite in lista
# for char in range(1,nr_letters+1):
#     password_list += random.choice(letters)
# #adaugam numarul de simboluri dorite in lista
# for symb in range(1,nr_symbols+1):
#     password_list += random.choice(symbols)
# # adaugam numarul de numere dorite in lista
# for number in range(1,nr_numbers+1):
#     password_list += random.choice(numbers)
#
# #folosim metoda random.shuffle pentru a amesteca toate elementele din lista
# random.shuffle(password_list)
# print(password_list)
# #creem parola finala
# final_password = ''
# #transformam lista prelucrata intr-un string
# for char in password_list:
#     final_password += char
# print(final_password)
