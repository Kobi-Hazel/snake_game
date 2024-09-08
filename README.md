# Snake Game

This is a classic Snake Game implemented using Python's `turtle` module. The goal of the game is to control the snake and eat the food to increase the score. The snake grows as it eats, and the game ends when the snake hits the wall or its own body.

## Features
- Snake movement with up, down, left, and right arrow keys
- Food appears at random positions on the screen
- Score increases as the snake eats food
- Snake grows longer as it eats
- Game restarts when the snake hits the wall or itself

## Prerequisites

To run this game, you will need:

- Python 3.x
- `turtle` module (comes pre-installed with Python)
- Optional: Install any IDE or text editor to run the code (e.g., VSCode, PyCharm)

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/snake-game.git

2. Navigate to the project folder:
   ```bash
   cd snake-game
   
3. Run the game
   ```bash
   python main.py

## Game Instructions
- Use the arrow keys to move the snake:
  - Up: Move the snake upwards
  - Down: Move the snake downwards
  - Left: Move the snake left
  - Right: Move the snake right
- The snake will move continuously in the last pressed direction.
- Eat the food to increase your score and grow the snake.
- Avoid hitting the walls or your own snake's body. The game will reset if you do.

## File Structure
- main.py: The main game loop and setup.
- snake.py: The Snake class, handling snake movement and behavior.
- food.py: The Food class, responsible for generating food at random positions.
- scoreboard.py: The Scoreboard class, tracking and displaying the player's score.

## Example Gameplay

