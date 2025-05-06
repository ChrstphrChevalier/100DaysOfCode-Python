import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv("50_states.csv")
found_states = []

answer_user = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

while len(found_states) < 50:
    if len(found_states) > 0:
        answer_user = screen.textinput(title=f"{len(found_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_user == 'Exit':
        missed_states = [state for state in states_data.state if state not in found_states]
        missed_states_df = pd.DataFrame(missed_states, columns=["State"])
        missed_states_df.to_csv("missed_states.csv")
        exit()

    if answer_user in states_data['state'].values and answer_user not in found_states:
        found_states.append(answer_user)
        state_row = states_data[states_data.state == answer_user]
        x = int(state_row.x.iloc[0])
        y = int(state_row.y.iloc[0])

        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(x, y)
        writer.write(answer_user, align="left", font=("Arial", 10, "normal"))
    
    elif answer_user is None or answer_user not in states_data["state"].values:
        continue

screen.exitonclick()