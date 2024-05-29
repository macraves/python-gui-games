"""Game Window Design"""

import time
from turtle import Screen
from ball_methods import Ball
from show_border import Border


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PAD_UPPER, PAD_BOTTOM = 10, 25
PAD_SIDES = 10


UPPRER_BOUNDRY = (SCREEN_HEIGHT // 2) - PAD_UPPER
BOTTOM_BOUNDRY = (SCREEN_HEIGHT // 2) - PAD_BOTTOM
SIDES_BOUNDRY = (SCREEN_WIDTH // 2) - PAD_SIDES

SCREEN = Screen()
SCREEN.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
SCREEN.title("BREAKOUT")
SCREEN.bgcolor("black")
SCREEN.tracer(0)

ball = Ball()


def draw_borders():
    """docs"""
    pen = Border()
    pen.bottom_line()
    pen.right_line()
    pen.left_line()
    pen.upper_line()


draw_borders()

GAME_ON = True
while GAME_ON:
    time.sleep(ball.ball_speed)
    SCREEN.update()
    ball.move()
    # Sides Collision
    if ball.xcor() > SIDES_BOUNDRY or ball.xcor() < -SIDES_BOUNDRY:
        ball.bounce_x()
    if ball.ycor() > UPPRER_BOUNDRY or ball.ycor() < -BOTTOM_BOUNDRY:
        ball.bounce_y()


SCREEN.exitonclick()
