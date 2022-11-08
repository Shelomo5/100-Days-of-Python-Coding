from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("White")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        #speed of the ball
        self.move_speed = 0.1

    # function causes ball to move to top right corner of screen
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # when ball bounces off wall we reverse y direction
    def bounce_y(self):
        self.y_move *= -1

    # when ball bounces off wall we reverse x direction of ball movement
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # ball placed back in middle and moves toward opposite player
    def reset_position(self):
        self.goto(0, 0)
        # reset ball speed
        self.move_speed = 0.1
        self.bounce_x()