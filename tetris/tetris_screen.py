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
        self.grid.append([1 for _ in range(12)])
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
        self.starting_row = shape.height

    def reset_grid_as_shape_height(self, shape: Shape):
        """Grid upper rows value set to 0"""
        if self.starting_row - shape.height < 0:
            return
        row = self.starting_row - shape.height
        for y, lst in enumerate(shape.block):
            for x, col in enumerate(lst):
                if self.grid[row + y][self.starting_col + x] == col:
                    self.grid[row + y][self.starting_col + x] = 0

    def draw_grid(self, shape: Shape):
        """Put shape in in center of length and starts convert
        0s to 1s according given Shape"""
        column = self.start_in_column(shape=shape)
        # put shape values into grid
        self.place_matrix_value(row=self.starting_row, col=column, shape=shape)
        self.starting_row = shape.height

    def is_under_the_shape_bottom_block_empty(self, shape: Shape):
        """_summary_"""
        # shape_bottom_area = shape.shape_bottom_area()
        return self.grid[self.starting_row][
            self.starting_col : self.starting_col + shape.width
        ] == [0 for _ in range(shape.width)]

    def is_shape_area_fit_in_next_area(self, shape: Shape):
        """Shape area can be fitted if it moved"""
        if self.starting_row + shape.height > len(self.grid):
            return

    def move_down(self, shape: Shape):
        """Updates starting point value according height of shape"""
        if self.starting_row == len(self.grid) - 1:
            return

        if not self.is_under_the_shape_bottom_block_empty(shape=shape):
            return
        self.place_matrix_value(
            row=self.starting_row, col=self.starting_col, shape=shape
        )

        self.reset_grid_as_shape_height(shape=shape)


def pretty_grid(screen: Window):
    """docs"""
    grid = screen.grid
    map_grid = map(lambda item: f"{item[0]}. {item[1]}", enumerate(grid))
    return "\n".join(map_grid)


def place_shape():
    """docs"""
    block = Shape()
    block.create_specific_shape("cube")
    pprint(block.block)
    print("GRID")
    window = Window(width=WIDTH, height=HEIGHT)
    window.draw_grid(shape=block)
    print(pretty_grid(window))
    print("Move BLOCK")
    window.move_down(shape=block)
    # window.move_down(shape=block)
    print(pretty_grid(window))


place_shape()
