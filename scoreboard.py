# Import necessary module
from turtle import Turtle

# Constants for text alignment and font style
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")

class Scoreboard(Turtle):
    """
    Scoreboard class to display and manage the score and high score.
    Inherits from the Turtle class to use turtle graphics for display.
    """
    def __init__(self):
        """Initialize the scoreboard with starting values and display settings."""
        super().__init__()                 # Initialize the Turtle base class
        self.penup()                       # Disable drawing while moving
        self.pencolor("white")             # Set the text color to white
        self.hideturtle()                  # Hide the turtle cursor
        self.goto(0, 270)                  # Position the scoreboard at the top center
        self.high_score = self.load_high_score()  # Load the high score from a file
        self.score = 0                     # Initialize the current score
        self.write_score()                # Display the initial scores
        self.speed("fastest")              # Set the drawing speed to the fastest

    def load_high_score(self):
        """
        Load the high score from a file.
        
        Returns:
            int: The high score read from the file.
        """
        try:
            with open("high_score.txt", mode="r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0  # Return 0 if the file does not exist

    def write_score(self):
        """Clear the current score and display the updated score and high score."""
        self.clear()  # Clear previous score display
        self.write(
            arg=f"Score: {self.score} High Score: {self.high_score}",
            move=False,
            align=ALIGNMENT,
            font=FONT
        )

    def reset_scoreboard(self):
        """
        Reset the scoreboard to the initial state and update the high score if needed.
        """
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0  # Reset current score to 0
        self.write_score()  # Update the displayed scores

    def update(self):
        """
        Increment the score and update the display.
        """
        self.score += 1
        self.write_score()
