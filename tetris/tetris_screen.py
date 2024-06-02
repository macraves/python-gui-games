"""taking into account dynamic shaping"""

from pprint import pprint
from turtle import Screen
from tetris_shape import Shape

BGCOLOR = "black"
PLAYABLE_AREA = "orange"

WIDTH = 600
HEIGHT = 800


class Window:
    """docs"""

    def __init__(self, width, height, square_size=1):
        self.width = width
        self.height = height
        self.strech = square_size
        self.window = Screen()
        self.window.title("Tetris By Grids")
        self.window.setup(width=self.width, height=self.height)
        self.window.bgcolor("black")
        self.grid = [[0 for _ in range(12)] for _ in range(6)]
        self.starting_row = 0
        self.starting_col = 0

    def start_in_column(self, shape: Shape):
        """Calculate grid width to place Shape in the middle of the screen"""
        half_screen_width = len(self.grid[0]) // 2
        half_shape_width = shape.width // 2
        column = half_screen_width - half_shape_width - 1
        self.starting_col = column
        return column

    def place_matrix_value(self, row, col, shape):
        """docs"""
        for y, lst in enumerate(shape.block):
            for x, value in enumerate(lst):
                self.grid[row + y][col + x] = value

    def draw_grid(self, shape: Shape):
        """Put shape in in center of length and starts convert
        0s to 1s according given Shape"""
        column = self.start_in_column(shape=shape)
        # put shape values into grid
        self.place_matrix_value(row=self.starting_row, col=column, shape=shape)
        self.starting_row = shape.height

    def move_down(self, shape: Shape):
        """Updates starting point value according height of shape"""
        if self.grid[self.starting_row][
            self.starting_col : self.starting_col + shape.width
        ] == [0 for _ in range(shape.width)]:
            self.place_matrix_value(
                row=self.starting_row, col=self.starting_col, shape=shape
            )


def place_shape():
    """docs"""
    block = Shape()
    block.create_cube()
    pprint(block.block)
    print("GRID")
    window = Window(width=WIDTH, height=HEIGHT)
    window.draw_grid(shape=block)
    pprint(window.grid)
    print("Move BLOCK")
    window.move_down(shape=block)
    pprint(window.grid)


place_shape()
