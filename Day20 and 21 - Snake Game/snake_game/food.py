import random
from turtle import Turtle

#inherited from Turtle class
class Food(Turtle):
    #creates food
    def __init__(self):
        super().__init__()
        self.shape("circle")
        #to ensure it doesn't draw
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed('fastest')
        #calls method below
        self.refresh()

    #creates random location and gets food to go to new location
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)