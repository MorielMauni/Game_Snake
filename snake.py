# Imports
import turtle
from turtle import Turtle

STRATING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create the Snake body and make in more 'snakey'"""
        for position in STRATING_POSITION:
            self.add_segment(position)


    def add_segment(self, position):
        '''
        Add a segment to the snake when eat food
        '''
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        '''
        Extend a NEW segment to the snake when eat food
        '''
        self.add_segment(self.segments[-1].position())

    def snake_reset(self):
        """
        Clear the screen from lost games and creates a new game
        """
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        """Snake Movement: make all the parts of the snake to always moves forward"""
        #                      start,              stop, step
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Movement of the snake for the '.lister'
    # Make sure you can't go backwards
    def up(self):
        """Makes the snake go up and can't go down"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        """Makes the snake go down and can't go up"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        """Makes the snake go left and can't go right"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        """Makes the snake go right and can't go left"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)