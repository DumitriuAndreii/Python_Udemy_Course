# Ex 1 - Random module
# import random
# random_integer = random.randint(1,10)
# print(random_integer)
#
# random_float = random.random()
# print(random_float)
#
# love_score  = random.randint(1,100)
# print(f"your love score is {love_score}")

# Ex 2 - cap si pajura, noi suntem banul si stema
# import random

# a = random.randint(0,1)
# if a == 0:
#     print("you got head :) ")
# else:
#     print("you got tails :(")

# Ex 3 - Modelarea listelor

# states_of_america = ["delaware", "pennsylvania", "las vegas"]
# states_of_america[1] = "pencilvania"
# print(states_of_america[1])
# states_of_america.append("Andreiland")
# print(states_of_america)
# states_of_america.extend(["Andreiboss", "Madagascar"])
# print(states_of_america)

# Ex 4 - Ruleta ruseasca
# import random
#
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(",")
# print(names)
# num_names = len(names)
#1 falit = random.randint(0,num_names-1)

#2 falit = random.choice(names)

# print(f"cel care v-a fi falimentat in aceasta seara esteeee {names[falit]}")

# Ex 5 - ceva cu legume

# fruits = ["strawberries", "spinach", "kale", "nectarines", "apples","Grapes","peaches","cherries","pears"]
# vegetables = ["spinach","kale","tomatoes","celery","potatoes"]
#
# dirty_dozen = [fruits,vegetables]
# print(dirty_dozen)

#Ex 6  - treasure hunt
#
# row1 = ["⬜️10", "⬜️11", "⬜️12"]
# row2 = ["⬜️20", "⬜️21", "⬜️22"]
# row3 = ["⬜️30", "⬜️31", "⬜️32"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
#
# horizontal = int(position[0])
# vertical = int(position[1])
#
# selected_row = (map[vertical-1])
# selected_row[horizontal - 1] = 'X'
#
# #2  map[vertical- 1][horizontal - 1] = "x"
# print(f"{row1}\n{row2}\n{row3}")


#Ex 7 - FINAL PROJECT OF THE DAY ( CIO-CA-NEL )
# import random
#
# rock = "piatraaaa"
# paper = "hartieeee"
# scissors = "foarceceeee"
# ciocanel_list = [rock,paper,scissors]
# print("Welcome to rock,paper, scissors!! ")
# player = int(input("Type 0 for rock, 1 for paper and 2 for scissors   "))
# print(ciocanel_list[player])
# print("Computer chose")
#
# computer = random.randint(0,2)
# print(ciocanel_list[computer])
# if player == 0 and computer == 0:
#     print("it's a tie")
# if player == 0 and computer == 1:
#     print("computer wins")
# if player == 0 and computer == 2:
#     print("you win")
# if player == 1 and computer == 0:
#     print("you win")
# if player == 1 and computer == 1:
#     print("it's a tie")
# if player == 1 and computer == 2:
#     print("computer wins")
# if player == 2 and computer == 0:
#     print("computer wins")
# if player == 2 and computer == 1:
#     print("you win")
# if player == 2 and computer == 2:
#     print("it's a tie")

#V2
# import random
#
# rock = "piatraaaa"
# paper = "hartieeee"
# scissors = "foarceceeee"
# ciocanel_list = [rock,paper,scissors]
# print("Welcome to rock,paper, scissors!! ")
# player = int(input("Type 0 for rock, 1 for paper and 2 for scissors   "))
# if player >2 or player < 0:
#     print("game over you lose bcs you do not knwo the numbers")
# else:
#     print(ciocanel_list[player])
#     print("Computer chose")
#     computer = random.randint(0,2)
#     print(ciocanel_list[computer])
#     if player == 0 and computer == 2:
#         print('you win')
#     elif player == 2 and computer == 0:
#         print("you lose")
#     elif computer > player:
#         print("you lose")
#     elif computer == player:
#         print("it s a tie")
#     elif player > computer:
#         print("you win")