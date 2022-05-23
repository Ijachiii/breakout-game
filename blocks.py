from turtle import Turtle
import random


col = ["red", "green", "yellow", "orange", "purple"]


class Blocks(Turtle):
    tx, ty = -250, 300

    def __init__(self, x, y):
        super().__init__()
        self.white = False
        self.penup()
        self.goto(x, y)
        self.color(random.choice(col))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2.5)






#        for i in range(-80, 170):
#            if i % 30 == 0:
#                new_block = Turtle("square")
#                new_block.shapesize(stretch_wid=1, stretch_len=4)
#                new_block.penup()
#                new_block.color(random.choice(col))
#                x = i
#                y = i
#                new_block.goto(x, y)
#                self.all_blocks.append(new_block)