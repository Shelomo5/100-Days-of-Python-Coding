from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

#No inheritance since mutiplicity of instances needed, objects created within class
class Snake:
    def __init__(self):
        self.segments = []
        #calls create_snake function below when snake object is initiated
        self.create_snake()
        ##first segment assoicated in list to self.head
        self.head = self.segments[0]

    def create_snake(self):

        #position is a tuple with x,y coordinate
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    #position where new segment(Turtle object) is added
    def add_segment(self, position):
        #defined new_segment as a Turtle object,
        # and so all relevant methods are available to it.
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        # go to tuple location
        new_segment.goto(position)
        # add to list
        self.segments.append(new_segment)

    #restores snake to start configuration
    def reset(self):
        #loops through and moves segments from previous turn off the
        # screen so they don't appear in current turn
        for seg in self.segments:
            seg.goto(1000, 1000)
        #removes all items from list
        self.segments.clear()
        #creates 3 segment snake
        self.create_snake()
        #first segment assoicated in list to self.head
        self.head = self.segments[0]

    def extend(self):
        #add a new segment to the last segment of list
        #position() method from turtle class which lets us know where last segment is
        self.add_segment(self.segments[-1].position())

    def move(self):
        # for loop gets segments to move in unison,
        # Take the number of segments and iterate with -1 step size
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # new coordinates of second to last segment's position, 2-1 is second to last segment
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # grab last segment (bc iterating step down 2,1,0) and instruct it
            # to go to position (x and y coordinates) of second to last segment
            self.segments[seg_num].goto(new_x, new_y)
        # 0 is not included in for loop hence why index 0 has to be moved forward outside for loop
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # it can move up for all direction except if heading is down
        if self.head.heading() != DOWN:
            # grab first segment and set its direction up
            self.head.setheading(UP)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)