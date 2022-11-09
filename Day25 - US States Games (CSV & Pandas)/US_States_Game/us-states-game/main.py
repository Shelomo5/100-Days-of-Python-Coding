import turtle
from turtle import Turtle, Screen
import pandas as pd

#create screen obbject
screen = Screen()
screen.title("Guess The U.S. States")
#image path
image = "blank_states_img.gif"
#loading image path into the screen
screen.addshape(image)
turtle.shape(image)

# making dataframe
df = pd.read_csv("50_states.csv")

#Putting csv state column into a list
all_states = df.state.to_list()

#list of states guessed by user
guessed_states = []

while len(guessed_states) < 50:
    # allows for user text input to enter state name
    #.title makes first letter in cap
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if user_answer == "Exit":
        # list of missing states not guessed by user
        unfound_states = []
        for state in all_states:
            if state not in guessed_states:
                unfound_states.append(state)
        #creating new data frame of missing states
        new_data = pd.DataFrame(unfound_states)
        #save it as a CSV list
        new_data.to_csv("states_to_learn.csv")
        break
    #since all_states was converted into a list we can check if answer is in it
    if user_answer in all_states:
        guessed_states.append(user_answer)
        #creating tutle to write state name at x,y coordinates
        t = Turtle()
        #so shape of turtle isn't seen
        t.hideturtle()
        #so it doesn't do any drawing
        t.penup()
        #row of data extracted where answer state is equal to the state in the list
        state_row = df[df.state == user_answer]
        #go to a specific coordinate
        # x,y coordinates can be found using name of the columns of csv
        t.goto(int(state_row.x), int(state_row.y))
        # state name placed at coordinate
        t.write(user_answer)


