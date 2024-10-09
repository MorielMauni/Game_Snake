from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        '''
        Gives the food the Shape, penup, shapesize to smaller, color, speed and random X and Y each time
        '''
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.refresh()

    def refresh(self):
        '''
        every time the snake "eat" a circle, it moved to a new random location
        '''
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)