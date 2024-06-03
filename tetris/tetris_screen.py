"""taking into account dynamic shaping"""

from turtle import Screen
from tetris_shape import Shape

BGCOLOR = "black"
PLAYABLE_AREA = "orange"


class Window:
    """docs"""

    count = 0
    flag = True

    def __init__(self, width, height, square_size=1):
        self.width = width
        self.height = height
        self.strech = square_size
        self.window = Screen()
        self.window.title("Tetris By Grids")
        self.window.setup(width=self.width, height=self.height)
        self.window.bgcolor("black")
        self.grid = [[0 for _ in range(12)] for _ in range(24)]
        self.starting_row = 0
        self.starting_col = 0

    def start_in_column(self, shape: Shape):
        """Calculate grid width to place Shape in the middle of the screen"""
        half_screen_width = len(self.grid[0]) // 2
        half_shape_width = shape.width // 2
        column = half_screen_width - half_shape_width - 1
        self.starting_col = column

    def place_matrix_value(self, row, col, shape):
        """docs"""
        self.reset_previous_grid_row(shape=shape)
        for y, lst in enumerate((shape.block)):
            for x, value in enumerate(lst):
                self.grid[row + y][col + x] = value
        self.starting_row += 1
        if Window.flag:
            print(f"{Window.count}. Placed\n{self.pretty_grid()}")

    def reset_previous_grid_row(self, shape: Shape):
        """docs"""
        if self.starting_row - 1 < 0:
            return
        row_to_check = self.starting_row - 1
        col_to_start = self.starting_col
        for y, row in enumerate(shape.block):
            for x, value in enumerate(row):
                if self.grid[y + row_to_check][x + col_to_start] == value:
                    self.grid[y + row_to_check][x + col_to_start] = 0
        if Window.flag:
            print(f"{Window.count}. Reseted\n{self.pretty_grid()}")

    def does_the_bottom_of_the_shape_fit_on_the_line_below(self, row, shape: Shape):
        """_summary_"""
        shape_bottom_row_len = shape.shape_bottom_list_len()
        return self.grid[row][
            self.starting_col : self.starting_col + shape_bottom_row_len
        ] == [0 for _ in range(shape_bottom_row_len)]

    def does_shape_width_fit_next_row(self, shape):
        """docs"""
        next_row = self.starting_row + shape.height - 1
        if next_row > len(self.grid) - 1:
            return
        if not self.does_the_bottom_of_the_shape_fit_on_the_line_below(
            row=next_row, shape=shape
        ):
            return False
        return self.grid[next_row][
            self.starting_col : self.starting_col + shape.width
        ] == [0 for _ in range(shape.width)]

    def move_down(self, shape: Shape):
        """Updates starting point value according height of shape"""
        if self.starting_row > len(self.grid) - 1:
            return
        if not self.does_shape_width_fit_next_row(shape=shape):
            return

        self.place_matrix_value(
            row=self.starting_row, col=self.starting_col, shape=shape
        )

    def move_left(self, shape: Shape):
        """Set column -1"""
        if self.starting_col > 0:
            self.reset_previous_grid_row(shape=shape)
            self.starting_col -= 1

    def move_right(self, shape: Shape):
        """Set column -1"""
        if self.starting_col + shape.width < len(self.grid[0]):
            self.reset_previous_grid_row(shape=shape)
            self.starting_col += 1

    def clockwise(self, shape: Shape):
        """Rotate by horizontally"""
        self.reset_previous_grid_row(shape=shape)
        shape.clockwise()

    def anti_clockwise(self, shape: Shape):
        """Rotate by vertically"""
        self.reset_previous_grid_row(shape=shape)
        shape.anti_clockwise()

    def pretty_grid(self):
        """docs"""
        if not Window.flag:
            return None
        Window.count += 1
        map_grid = map(lambda item: f"{item[0]}. {item[1]}", enumerate(self.grid))
        return "\n".join(map_grid)


def place_shape():
    """docs"""
    block = Shape()
    block.create_specific_shape("L")
    # pprint(block.block)
    window = Window(width=600, height=800)
    # print(f"New grid start row index: {window.starting_row}")
    window.move_down(shape=block)
    # print(window.pretty_grid())
    # print(f"New grid current row index: {window.starting_row}")
    window.move_down(shape=block)
    # print(f"New grid current row index: {window.starting_row}")
    window.move_down(shape=block)
    window.move_down(shape=block)
    window.move_down(shape=block)
    window.move_down(shape=block)
    window.move_down(shape=block)
    window.move_down(shape=block)
    window.move_down(shape=block)
    # print(f"Last view\n{window.pretty_grid()}")
