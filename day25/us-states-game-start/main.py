import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

# def get_mouse_click_coordinate(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coordinate)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

game_is_on = 1

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 guessed", prompt="guess another state").title()
    # answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:

        state_data = data[data["state"] == answer_state]
        guessed_states.append(answer_state)
        print(state_data.state.item())
        printable_state_verified = turtle.Turtle()
        printable_state_verified.hideturtle()
        printable_state_verified.penup()
        printable_state_verified.goto(int(state_data.x), int(state_data.y))
        printable_state_verified.write(answer_state)  # printable_state_verified.write(state_data.state.item())