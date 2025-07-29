from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 12, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score += 5
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 12, "normal"))

    def increase_score_bonus(self):
        self.score += 10
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 12, "normal"))

    def game_over(self):
        self.color("white")
        self.penup()
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", move=False, align="center", font=("Arial", 22, "normal"))
