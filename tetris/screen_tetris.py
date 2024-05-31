"""Screen and Border Optimazation"""

from turtle import Screen
from grid_lines import Square, Line


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


square = Square(width=2, height=2)
print([item.position() for item in square.squares])
line = Line()

line.go_right(square=square)
line.go_left(square=square)


# SCREEN.update()

SCREEN.exitonclick()
