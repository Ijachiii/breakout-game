from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-260, 260)
        self.write(f"Score: {self.score}", align="left", font=("Courier", 20, "normal"))

    def point(self):
        self.score += 4
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=("Courier", 18, "normal"))

    def win(self):
        self.goto(0, 0)
        self.write(f"YOU WIN!!\nYour Score: {self.score}", align="center", font =("Courier", 18, "normal"))
