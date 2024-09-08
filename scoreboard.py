from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor("white")
        self.hideturtle()
        self.goto(0, 270)
        with open("high_score.txt", mode="r") as file:
             self.high_score = int(file.read())
        self.score = 0
        self.write_score()
        self.speed("fastest")

    def write_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.write_score()


    def update(self):
        self.score += 1
        self.write_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
