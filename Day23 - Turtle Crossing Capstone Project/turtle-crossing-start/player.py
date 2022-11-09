from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90

#Turtle being controlled to cross the road
class Player(Turtle):

    def __init__(self):
        #executes init() method in Turtle class which creates a Turtle object,
        # an "instance" of the Turtle class assigned to self
        super().__init__()
        self.shape("turtle")
        self.penup()
        #sets starting position which is a tuple
        self.goto_starting_line()
        self.setheading(UP)

    #function allows turtle to move up
    def up(self):
        self.forward(MOVE_DISTANCE)

    #function which detects when turtle reaches top of screen
    def reached_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def goto_starting_line(self):
        self.goto(STARTING_POSITION)

