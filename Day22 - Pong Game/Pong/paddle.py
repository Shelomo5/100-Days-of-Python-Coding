from turtle import Turtle

#class creates paddles
class Paddle(Turtle):
    #position tupple passed in when Paddle class initialized
    def __init__(self, position):
        #super().__init__() calls the initialization method in the Turtle class,
        # which creates a Turtle object. This Turtle object is assigned to the variable self,
        # so Paddle object created becomes a Turtle object -
        # along with any additional attributes you create in the Paddle class.
        super().__init__()
        self.shape("square")
        self.color("White")
        #All turtles start 20 by 20 but we want 100 by 20, so stretch width by 5
        self.shapesize(stretch_wid=5, stretch_len=1)
        #ensures line isn't drawn as it moves
        self.penup()
        self.goto(position)

    #function to shift paddle upward and downward
    def go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)
        #prevents paddle y coordinate to leave screen
        else:
            self.goto(self.xcor(), 250)

    def go_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
        else:
            self.goto(self.xcor(), -250)