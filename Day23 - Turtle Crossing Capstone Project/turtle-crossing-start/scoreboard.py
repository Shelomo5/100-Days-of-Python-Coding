FONT = ("Courier", 18, "normal")
from turtle import Turtle

#Writes level and Game Over sequence

class Scoreboard(Turtle):
    #Our Scoreboard instantiation is able to do everything a Turtle class can do
    def __init__(self):
        super().__init__()
        #level attribute
        self.level = 0
        #hides turtle/arrow so it can be used just for drawing
        self.hideturtle()
        #so it doesn't draw when moved
        self.penup()
        #moves scoreboard to top left of screen
        self.goto(-290, 270)
        self.updates_scoreboard()

    # writes current level player is on
    def updates_scoreboard(self):
        #clear scoreboard
        self.clear()
        #write current score
        self.write(f"Level: {self.level}", align="left", font=FONT)

    #increases level by increment of 1
    def level_up(self):
        self.level += 1
        self.updates_scoreboard()
    #displays end of game
    def end_game(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)




