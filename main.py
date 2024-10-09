# Imports
from logging import fatal
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
import time

# Screen 'Settings'
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Game: Snake")
screen.tracer(0)

snake= Snake()
# Snake Food
food = Food()
score = Score()

# Listener for the key inputs
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")

# While Loop for the game
game_is_on =True
while game_is_on:
    # Make is smoother
    screen.update()
    # Delay for the snake body
    time.sleep(0.1)
    snake.move()
    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        # Snake get extended for each time he eats
        snake.extend()
        # Scoreboard
        score.increase_score()
    # Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Collision with tail
    for segment in snake.segments[1:]:
        # Exclude the head of the snake
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()