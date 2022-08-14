import turtle
import pandas


# UI
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# csv data
data = pandas.read_csv("50_states.csv")
states = data.state
states = states.to_list()


guess_there = True
state_correct = 0

states_guessed = []

while guess_there:
    answer_state = turtle.textinput(title=f"{state_correct}/50 States Correct", prompt="What's another state name?").title()

    if state_correct == 50:
        guess_there = False

    if answer_state in states:
        state_correct += 1

        # get x and y values using of state name
        state_data = data[data.state == answer_state]
        x = int(state_data.x)
        y = int(state_data["y"])
        print((x, y))

        # write state name on screen
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(x, y)
        t.write(answer_state)
        states_guessed.append(answer_state)
    elif answer_state == "Exit":
        guess_there = False
        missing_states = []
        for state in states:
            if state not in states_guessed:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")















"""

# get coordinates on
def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()

"""