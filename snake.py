# Import necessary module
from turtle import Turtle

# Constants for movement and direction
MOVE_DISTANCE = 20  # Distance the snake moves in each step
UP = 90             # Upward direction (90 degrees)
DOWN = 270          # Downward direction (270 degrees)
LEFT = 180          # Leftward direction (180 degrees)
RIGHT = 0           # Rightward direction (0 degrees)

# Initial positions of the snake segments
POSITION = [(0, 0), (0, -20), (0, -40)]


class Snake:
    """
    Snake class to represent the snake object and manage its movement, growth, 
    and reset behavior in the game.
    """
    def __init__(self):
        """Initialize the snake with segments and set the head."""
        self.segments = []   # List to hold all segments of the snake
        self.create_snake()  # Create the initial snake
        self.head = self.segments[0]  # The first segment is the head

    def create_snake(self):
        """Create the snake by adding initial segments."""
        for position in POSITION:
            self.add_segment(position)  # Add each segment to the snake

    def add_segment(self, position):
        """
        Add a new segment to the snake at the given position.
        
        Args:
            position (tuple): Coordinates where the new segment should be added.
        """
        new_turtle = Turtle("square")  # Create a new turtle object for each segment
        new_turtle.color("white")      # Set the color to white
        new_turtle.penup()             # Disable drawing a line as it moves
        new_turtle.goto(position)      # Move the segment to the specified position
        self.segments.append(new_turtle)  # Add the segment to the list

    def move(self):
        """Move the snake forward by updating the position of each segment."""
        # Move each segment except the head to the position of the previous segment
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()  # Get the x-coordinate of the previous segment
            new_y = self.segments[segment - 1].ycor()  # Get the y-coordinate of the previous segment
            self.segments[segment].goto(new_x, new_y)  # Move the current segment to the previous segment's position
        self.head.forward(MOVE_DISTANCE)  # Move the head forward

    def reset(self):
        """
        Reset the snake when it collides with a wall or its own body.
        Moves all segments off-screen and recreates the snake.
        """
        for segment in self.segments:
            segment.goto(1000, 1000)  # Move segments off-screen
        self.segments.clear()         # Clear the segments list
        self.create_snake()           # Recreate the snake with initial segments
        self.head = self.segments[0]  # Reset the head to the first segment

    def up(self):
        """Change the snake's direction to up if it's not already moving down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change the snake's direction to down if it's not already moving up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change the snake's direction to left if it's not already moving right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change the snake's direction to right if it's not already moving left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        """
        Add a new segment to the snake when it eats food.
        The new segment is added at the position of the last segment.
        """
        self.add_segment(self.segments[-1].position())  # Add a new segment at the tail's position
