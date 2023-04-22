import turtle
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game for Chanda")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_status = True
while game_status:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        score.update()
        snake.extend()
    if snake.head.xcor() > 295 or snake.head.ycor() < -295 or snake.head.xcor() < -295 or snake.head.ycor() > 295:
        score.reset()
        snake.reset()
    for instance in snake.instances[1:]:
        if snake.head.distance(instance) < 10:
            game_status = False
            score.reset()
            snake.reset()

screen.exitonclick()
