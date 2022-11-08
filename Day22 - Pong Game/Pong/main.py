from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Setting up screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title('Pong')
#turns off animation
screen.tracer(0)


#Paddle objected instantiated and tuple passed in as location
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


#paddles listen to key strokes to go up and down
screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    #delays time in between screen updates, the smaller the delay the daster the ball
    time.sleep(ball.move_speed)
    #manually updates screen and refresh it
    screen.update()
    #everytime loop runs ball moves by one pixel
    ball.move()
    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.xcor() == 330 and ball.distance(r_paddle) < 63) or (ball.xcor() == -330 and ball.distance(l_paddle) < 63):
        ball.bounce_x()



    #if ball goes past edge of x-axis of R paddle reset ball to the middle
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()


#ensures screen doesn't exit unless you click screen
screen.exitonclick()

