import pandas as pd
import turtle
from turtle import Turtle, Screen

states = pd.read_csv("/home/beast/100Days/us_states/50_states.csv")
screen = Screen()
screen.title("U.S. States Game")

image = "/home/beast/100Days/us_states/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = Turtle()
writer.pencolor("black")
writer.hideturtle()

correct_guess = []
all_states = states.state.to_list()
while len(correct_guess) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guess)}/50 states correct", prompt="What's another state's name?")
    
    if answer_state == "Exit":
        #List comprehensions
        missing_states = [state for state in all_states if state not in correct_guess]
        # missing_states = []
        # for state in all_states:
        #     if state not in correct_guess:
        #         missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("/home/beast/100Days/us_states/missing_states.csv")
        break
    
    if len(states[states.state == answer_state]) == 1 and answer_state not in correct_guess:
        state = states[states.state == answer_state.title()]
        correct_guess.append(answer_state.title())
        writer.penup()
        writer.goto(int(state.x), int(state.y))
        writer.pendown()
        writer.write(answer_state)

turtle.mainloop()

