"""
Unfinisher Project
Game Window Design
"""

import time
from turtle import Screen
from ball_methods import Ball

# from paddle_methods import Paddle
from paddle_segment import Paddles


from show_border import draw_borders

BIN = (0, -500)

TEST_SPEED = 0.05


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PAD_UPPER, PAD_BOTTOM = 10, 20
PAD_SIDES = 30

PROXIMITY = 20


UPPRER_BOUNDRY = (SCREEN_HEIGHT // 2) - PAD_UPPER - PROXIMITY
BOTTOM_BOUNDRY = (SCREEN_HEIGHT // 2) - PAD_BOTTOM - PROXIMITY
SIDES_BOUNDRY = (SCREEN_WIDTH // 2) - PAD_SIDES - PROXIMITY

PADDLE_BOUNDRY = SIDES_BOUNDRY + PROXIMITY
PADDLE_POSITIONS = [
    (-40, -(SCREEN_HEIGHT // 2 - 10)),
    (-20, -(SCREEN_HEIGHT // 2 - 10)),
    (0, -(SCREEN_HEIGHT // 2 - 10)),
    (20, -(SCREEN_HEIGHT // 2 - 10)),
    (40, -(SCREEN_HEIGHT // 2 - 10)),
]
BALL_POSITION = (0, -(SCREEN_HEIGHT // 2 - (PROXIMITY + 10)))

BLOCK_DISTANCE = [40, 60, 80]


STARTING_COR = (
    ((SCREEN_WIDTH) - 2 * PAD_SIDES) // 2,
    (SCREEN_HEIGHT - (PAD_UPPER + PAD_BOTTOM)) // 2,
)

BLOCK_CREATING_TIME = 60000
BLOCKS_MOVEMENT_SPEED = 5000
TIME_INTERVAL = 1000

SCREEN = Screen()
SCREEN.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
SCREEN.title("BREAKOUT")
SCREEN.bgcolor("black")
SCREEN.tracer(0)

ball = Ball(BALL_POSITION)
paddle = Paddles(PADDLE_POSITIONS)


SCREEN.listen()
SCREEN.onkey(lambda: paddle.go_right(PADDLE_BOUNDRY), "Right")
SCREEN.onkey(lambda: paddle.go_left(PADDLE_BOUNDRY), "Left")


def ball_paddle_collision(the_ball: Ball, board: list):
    """docs"""
    for segment in board.segments:
        if the_ball.distance(segment) < PROXIMITY:
            # snap_shot(the_ball)
            the_ball.bounce_y()
            board.extend()


GAME_ON = True
draw_borders(
    width=SCREEN_WIDTH,
    height=SCREEN_HEIGHT,
    pad_upper=PAD_UPPER,
    pad_bottom=PAD_BOTTOM,
    pad_sides=PAD_SIDES,
)


while GAME_ON:
    time.sleep(TEST_SPEED * 0.9)
    SCREEN.update()
    # test_ball_with_segments(paddle)
    ball.move()
    # block.blocks_move()

    # Sides Collision
    if ball.xcor() > SIDES_BOUNDRY or ball.xcor() < -SIDES_BOUNDRY:
        ball.bounce_x()
    # Top Collision
    if ball.ycor() > UPPRER_BOUNDRY:
        ball.bounce_y()

    ball_paddle_collision(ball, paddle)
    # ball_blocks_collision(ball)
    # Missing the ball
    if ball.ycor() < -(BOTTOM_BOUNDRY + 50):
        ball.goto(BIN)
        del ball
        # snap_shot(ball)
        MID_INDEX = len(paddle.segments) // 2
        middle = paddle.segments[MID_INDEX]
        ball = Ball(BALL_POSITION)
        # ball.reset_position(middle.position())
        paddle.shrink()


SCREEN.exitonclick()
