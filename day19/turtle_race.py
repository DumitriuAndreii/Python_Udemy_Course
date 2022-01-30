import random
import turtle
from turtle import Turtle, Screen


screen = Screen()
screen.bgcolor("#e9e2d2")
screen.title("Bine ati venit la cursele de testoase!")
is_race_on = False
screen.setup(width=1000, height=800)
user_bet = screen.textinput(title="Make your bet! ", prompt="Which turtle will win the race? Enter a color:  ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-200, -100, 0, 100, 200, 300]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-470, y=y_position[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 480:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!! ")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!! ")
            break
        random_distance = random.randint(0,30)
        turtle.forward(random_distance)






screen.exitonclick()