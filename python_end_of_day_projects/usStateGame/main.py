import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_name = data.state.to_list()

correct_guesses = []
missed_states = []


while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missed_states = [m for m in data.state if m not in correct_guesses]

        # for m in data.state:
        #     if m not in correct_guesses:
        #         missed_states.append(m)

        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states_name:
        correct_guesses.append(answer_state)
        state_data = data[data.state == answer_state]
        coordinates = turtle.Turtle()
        coordinates.speed("fastest")
        coordinates.hideturtle()
        coordinates.penup()
        # The Following is the same as state_data.x and state_data.y
        # iloc gets or sets a value to the specified place ------> iloc[row, column]
        coordinates.goto(state_data.iloc[0, 1], state_data.iloc[0, 2])
        coordinates.write(answer_state)
