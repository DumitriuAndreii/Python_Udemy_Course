import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
tim = Turtle()
tim.shape("turtle")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color
tim.speed("fastest")
## Provocarea 5

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

draw_spirograph(20)







# ## Provocarea 4
# tim.pensize(15)
# tim.speed("fastest")
# for _ in range(150):
#     tim.color(random_color())
#     tim.forward(25)
#     tim.setheading(random.choice([0, 90, 180, 270]))


## Provocarea 3
# de desenat un triunghi, patrat, pentagon ... etc din acelasi punct si cu o culoare diferita
# for latura in range(3,11):
#     tim.color(choice(colours))
#     for i in range(latura):
#         tim.forward(100)
#         tim.right(360/latura)


# import heroes
# print(heroes.gen())





screen = Screen()
screen.exitonclick()