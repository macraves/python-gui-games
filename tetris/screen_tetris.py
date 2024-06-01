"""Screen and Border Optimazation"""

import time
from turtle import Screen

from shape_matrix import Shape


WIDTH = 800
HEIGHT = 600
HALF_X = WIDTH // 2
HALY_Y = HEIGHT // 2

PAD = 30

SCREEN = Screen()
SCREEN.setup(width=WIDTH, height=HEIGHT)
SCREEN.title("Tetrs")
SCREEN.bgcolor("black")
SCREEN.tracer(0)

active_block = []


def create_shape():
    """docs"""
    shape = Shape()
    name = "t_shape"
    shape.create_the_shape(name)
    active_block.append((name, shape))


create_shape()
shape_name, block = active_block[0]


SCREEN.listen()
SCREEN.onkey(lambda: block.clockwise(shape_name), "Right")
GAME_SPEED = 0.5
GAME_ON = True


while GAME_ON:
    time.sleep(GAME_SPEED)
    SCREEN.update()
    block.move(shape_name=shape_name)

    # block.clockwise(shape_name)

# print([item.position() for item in square.squares])
# line = Line()

# line.go_right(square=square)
# line.go_left(square=square)
# line.right_down(square=square)
# line.right_up(square=square)
# line.left_up(square=square)
# line.left_down(square=square)


# SCREEN.update()

SCREEN.exitonclick()
