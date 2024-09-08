import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

score = 0
screen = Screen()
height = 600
width = 600
screen.setup(height=height, width=width)
screen.bgcolor("black")
screen.title(f"Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down,  key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update()
        snake.extend()

    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor())>280:
        scoreboard.reset_scoreboard()
        snake.reset()

    for part in snake.segments[1:]:
        if snake.head.distance(part) < 10:
            scoreboard.reset_scoreboard()
            snake.reset()

screen.exitonclick()
