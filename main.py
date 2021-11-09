from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Setting Graphical Interfaces 
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")
screen.addshape("apple.gif")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

# Importing classes
food = Food()
snake = Snake()
scoreboard = ScoreBoard()

# Control the snake with keys
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall

    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    # Detect collision with tail.

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()




screen.exitonclick()
