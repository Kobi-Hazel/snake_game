# Import necessary modules
import time
from turtle import Screen  # Turtle graphics for creating game window
from snake import Snake    # Snake class manages snake movement and segments
from food import Food      # Food class represents the food object
from scoreboard import Scoreboard  # Scoreboard class tracks and displays score

# Initialize screen settings
screen = Screen()
height = 600
width = 600
screen.setup(height=height, width=width)  # Set screen dimensions
screen.bgcolor("black")                   # Set background color to black
screen.title("Snake")                     # Set window title
screen.tracer(0)                          # Turn off animation for manual updates

# Create instances of Snake, Food, and Scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Set up screen key listeners for snake movement
screen.listen()
screen.onkey(fun=snake.up, key="Up")       # Move snake up when "Up" key is pressed
screen.onkey(fun=snake.down, key="Down")   # Move snake down when "Down" key is pressed
screen.onkey(fun=snake.left, key="Left")   # Move snake left when "Left" key is pressed
screen.onkey(fun=snake.right, key="Right") # Move snake right when "Right" key is pressed

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()                       # Update screen after each iteration
    time.sleep(0.1)                       # Control snake speed by adding a delay
    snake.move()                          # Move the snake

    # Detect collision with food
    if snake.head.distance(food) < 15:    # If snake head is close to food
        food.refresh()                    # Refresh food to a new location
        scoreboard.update()               # Increase the score
        snake.extend()                    # Extend snake by adding new segment

    # Detect collision with wall
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:  # If snake hits the wall
        scoreboard.reset_scoreboard()      # Reset scoreboard
        snake.reset()                      # Reset snake to starting position

    # Detect collision with tail
    for part in snake.segments[1:]:        # Loop through all segments except the head
        if snake.head.distance(part) < 10: # If head collides with any part of the body
            scoreboard.reset_scoreboard()  # Reset scoreboard
            snake.reset()                  # Reset snake

# Exit the game when the screen is clicked
screen.exitonclick()
