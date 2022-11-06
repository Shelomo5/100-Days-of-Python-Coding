from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
#screen background color
screen.bgcolor("black")
screen.title('Snake game')
#turns off tracer
screen.tracer(0)

#instantiating snake and food class
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_is_on = True
#loop through each segment and move them
while game_is_on:
    #screen updates every .1 sec to ensure snake moves as one piece
    screen.update()
    time.sleep(0.1)

    #method to move snake by one step
    snake.move()
    #detect collision with food if within 15 pixels
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        #updates scoreboard
        scoreboard.highest_score_update()
        #resets snake
        snake.reset()

    #Detect collision with tail.
    #Go through each tail segment
    for segment in snake.segments[1:]:
        #if head segment has distance less than 10 pixels from tail segments then game is over
        if snake.head.distance(segment) < 10:
            scoreboard.highest_score_update()
            snake.reset()

#ensures screen doesn't exit unless you click screen
screen.exitonclick()