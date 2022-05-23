from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=4)
        self.color("blue")
        self.penup()
        self.setpos(position)

    def go_right(self):
        new_x = self.xcor() + 30
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 30
        self.goto(new_x, self.ycor())
