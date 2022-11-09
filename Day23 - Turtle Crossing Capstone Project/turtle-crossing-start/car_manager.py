#why not use super class
import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# generates cars, stores them in a list, and moves them across the screen
# no inheritance since class creates and stores Turtle objects, itself it's not a Turtle object
class CarManager():

    def __init__(self):
        #list where car objects stored
        self.cars = []
        #initial car speed
        self.car_speed = STARTING_MOVE_DISTANCE

    #function which creates car objects
    def create_car(self):
        #ensures that a new car is made 1/6 time the while loop is ran
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            #initiating car object which is a Turtle object
            new_car = Turtle("square")
            #widen car by factor of two so it's rectangular
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            #pass in a random color
            new_car.color(random.choice(COLORS))
            # random y position
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            #appending new car object to list
            self.cars.append(new_car)

    def move_cars(self):
        #for each car in list of cars
        for car in self.cars:
            #move car backwards by 5 paces
            car.backward(self.car_speed)

    def speed_increase(self):
        #increases speed by 10
        self.car_speed += MOVE_INCREMENT


