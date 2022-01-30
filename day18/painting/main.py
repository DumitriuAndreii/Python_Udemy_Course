# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg',50)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import random
from turtle import Turtle, Screen, colormode
color_list = [(238, 250, 244), (187, 18, 44), (243, 231, 66), (210, 236, 242), (196, 75, 32),
 (218, 66, 107), (17, 124, 173), (196, 175, 17), (108, 181, 209), (12, 142, 88), (12, 166, 214), (210, 152, 96),
 (187, 41, 61), (241, 231, 2), (23, 39, 76), (77, 174, 94), (36, 44, 112), (215, 69, 50), (218, 130, 155),
 (124, 185, 119), (235, 165, 183), (5, 58, 39), (146, 209, 220), (8, 95, 55), (4, 86, 111), (162, 29, 27),
 (234, 171, 164), (162, 212, 176), (87, 22, 58), (182, 188, 209), (118, 122, 149), (94, 16, 15)]

colormode(255)


def draw_dot():
    # print(tim.xcor())
    tim.dot(20,random.choice(color_list))
    tim.fd(50)


tim = Turtle()
tim.shape("turtle")
tim.penup()
tim.speed("fastest")

tim.hideturtle()
# tim.setposition(-445,-445)
tim.setposition(-225,-225)
x = -225
y = -225
for coordinates in range(10):
    for i in range (10):
        draw_dot()
    y+=50
    tim.setposition(x,y)
tim.hideturtle()








screen = Screen()
screen.exitonclick()