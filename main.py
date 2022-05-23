from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
from blocks import Blocks
from random import choice
import time


paddle = Paddle((0, -250))
score = Score()

all_blocks = []
broken = []
tx, ty = -250, 230
dy = 1
dx = choice([-.5, .5])


screen = Screen()
screen.setup(width=550, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

for _ in range(6):
    for _ in range(10):
        block = Blocks(tx, ty)
        all_blocks.append(block)
        tx += 55
    ty -= 25
    tx = -250

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")


ball = Ball((0, -230))

game_is_on = True

while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.xcor() > 250 or ball.xcor() < -250:
        ball.bounce_x()

    if ball.ycor() < -280:
        game_is_on = False
        score.game_over()

    if len(broken) == len(all_blocks):
        game_is_on = False
        score.win()

    if ball.distance(paddle) < 30 and ball.ycor() < -235:
        ball.bounce_y()

    for block in all_blocks:
        if not block.white:
            if ball.distance(block) < 28:
                ball.bounce_y()
                block.color("black")
                block.white = True
                score.point()
                broken.append(block)


screen.exitonclick()
