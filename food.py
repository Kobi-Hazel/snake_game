# Import necessary modules
from turtle import Turtle
import random  # Random module to randomly place the food

class Food(Turtle):
    """
    Food class represents the food object in the Snake game.
    The food appears at random locations on the screen.
    """
    def __init__(self):
        """Initialize the food object with specific appearance and position."""
        super().__init__()                     # Inherit from the Turtle class
        self.shape("circle")                   # Set the shape of the food to a circle
        self.penup()                           # Disable drawing while moving
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Shrink the food size to half
        self.color("blue")                     # Set the color of the food to blue
        self.speed("fastest")                  # Set the speed of movement to the fastest
        self.refresh()                         # Position the food at a random location

    def refresh(self):
        """Move the food to a new random location on the screen."""
        random_x = random.randint(-280, 280)   # Generate random x-coordinate within screen bounds
        random_y = random.randint(-280, 280)   # Generate random y-coordinate within screen bounds
        self.goto(random_x, random_y)          # Move the food to the new random coordinates
