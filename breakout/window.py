"""Game Window Design"""

import time
from turtle import Screen
from ball_methods import Ball
from show_border import Pen


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
X_BOUNDRY = (SCREEN_WIDTH // 2) - 35
Y_BOUNDRY = (SCREEN_HEIGHT // 2) - 35

SCREEN = Screen()
SCREEN.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
SCREEN.title("BREAKOUT")
SCREEN.bgcolor("black")
# SCREEN.tracer(0)

ball = Ball()


def draw_borders():
    """docs"""
    pen = Pen()
    pen.bottom_line()
    pen.upper_line()
    pen.left_line()
    pen.right_line()


draw_borders()

GAME_ON = True
while GAME_ON:
    time.sleep(ball.ball_speed)
    SCREEN.update()

    # ball.ball_speed = 0.01
    # ball.move()


SCREEN.exitonclick()
