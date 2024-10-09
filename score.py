import turtle
from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 24, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write((f"Score: {self.score}"), align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.write((f"GAME OVER"), align=ALIGMENT, font=FONT)