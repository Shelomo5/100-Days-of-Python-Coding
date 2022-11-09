import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#creates a Player object, an instance of the Player class
#and assigns that object to the variable self
#this object is a turtle with the additional methods defined in Player class
player = Player()
# creates a CarManager object (an "instance" of the CarManager class),
# and assigns the object to the variable car_manager
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, 'Up')

game_is_on = True
#inside while loop code is updated every .1 seconds
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # create cars repeatedly since inside while loop
    car_manager.create_car()
    # move car
    car_manager.move_cars()

    #Detect collision with any car
    for car in car_manager.cars:
        #method from turtle module to detect if player is within 20 pixels of a car
        if car.distance(player) < 20:
            game_is_on = False
            #game over displayed to end game
            scoreboard.end_game()

    #call method which checks if player is at finish line
    if player.reached_finish_line():
        player.goto_starting_line()
        #if reaches finishes line speed increase function called so cars are faster
        car_manager.speed_increase()
        scoreboard.level_up()


#enables that screen exits when clic
screen.exitonclick()