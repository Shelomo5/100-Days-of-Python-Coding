from turtle import Turtle
FONT = ('Arial', 18, 'normal')
ALIGNMENT = "center"

class Scoreboard(Turtle):
    #Keeps track of score
    def __init__(self):
        super().__init__()
        # places scoreboard at the top
        self.goto(0, 270)
        self.score =0
        #open txt file with highest score number
        with open("data.txt") as data:
                #set highest score to number in txt file
                self.highest_score = int(data.read())
        self.color("white")
        # prevents arrow from showing up
        self.hideturtle()
        self.update_scoreboard()

    #Writes score
    def update_scoreboard(self):
        self.clear()
        self.write(f" Score: {self.score} Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    #changes highest score and resets score to 0
    def highest_score_update(self):
        #if level reached is greater than highest-score then it's the new highest score
        if self.highest_score < self.score:
            self.highest_score = self.score
            #updating data file & writing new highest_score
            with open("data.txt", mode="w") as data:
                data.write(str(self.highest_score))
        self.score = 0
        self.update_scoreboard()

    #Increases score by 1
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


