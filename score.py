import turtle
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset_score(self):
        """
        Reset the score, Update the High score
        """
        if self.score > self.high_score: # Making a new 'High Score'
            self.high_score = self.score
        self.score = 0 # Reset the score
        self.update_score()


    #def game_over(self):
    #    self.color("white")
    #    self.penup()
    #    self.goto(0, 0)
    #    self.write((f"GAME OVER"), align=ALIGNMENT, font=FONT)