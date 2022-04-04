from ctypes import alignment
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 250)
        self.hideturtle()
        self.color("white")
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        Turtle.clear(self)
        self.score += 1
        self.update()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over :(", False, align=ALIGNMENT, font=FONT)

