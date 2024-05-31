"""Screen and Border Optimazation"""

from turtle import Screen

from shape_design import Shape


WIDTH = 800
HEIGHT = 600
HALF_X = WIDTH // 2
HALY_Y = HEIGHT // 2

PAD = 30

SCREEN = Screen()
SCREEN.setup(width=WIDTH, height=HEIGHT)
SCREEN.title("Tetrs")
SCREEN.bgcolor("black")
# SCREEN.tracer(0)


shape = Shape()
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
