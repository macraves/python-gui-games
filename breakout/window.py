"""Game Window Design"""

import time
from turtle import Screen
from ball_methods import Ball, Turtle
from show_border import Border


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PAD_UPPER, PAD_BOTTOM = 10, 25
PAD_SIDES = 10

X_PROXIMITY = 20
Y_PROXIMITY = 20

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


def new_ball(current_ball: Turtle):
    """docs"""
    x_cor, y_cor = current_ball.xcor(), current_ball.ycor()
    the_ball = Ball()
    the_ball.goto(x_cor, y_cor)


GAME_ON = True
while GAME_ON:
    ball.speed = 0.01
    time.sleep(ball.ball_speed)
    SCREEN.update()
    ball.move()
    # Sides Collision
    if (
        ball.xcor() > SIDES_BOUNDRY - X_PROXIMITY
        or ball.xcor() < -SIDES_BOUNDRY + X_PROXIMITY
    ):
        new_ball(ball)
        ball.bounce_x()
    if (
        ball.ycor() > UPPRER_BOUNDRY - Y_PROXIMITY
        or ball.ycor() < -BOTTOM_BOUNDRY + Y_PROXIMITY
    ):
        new_ball(ball)
        ball.bounce_y()


SCREEN.exitonclick()
