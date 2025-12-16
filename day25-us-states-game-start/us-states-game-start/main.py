import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S States Game")
image = "us-states-game-start/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pd.read_csv("us-states-game-start/50_states.csv")
all_states = data.state.to_list()

guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_state)/50} Guess the State" , prompt="What's another states name").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("us-states-game-start/learn.csv")

        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        correct_state = data[answer_state == data.state]
        t.goto(int(correct_state.x), int(correct_state.y))
        t.write(answer_state)
    
turtle.mainloop()

