# print("hello")
# num_char = len("hello")
# print(num_char)

# def my_print():
#     print("hello")
#     print("panamera")
# my_print()

#Ex 1 - robotul care sare garduri
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# for n in range(6):
#     jump()

#Ex2 - proba 100m garduri cu garduri de diferite marimi
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#
#     while front_is_clear():
#         move()
#     turn_left()
#
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

#Ex3 - Rezolvarea labirintului
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# 
# while front_is_clear():
#     move()
# turn_left()
#
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
