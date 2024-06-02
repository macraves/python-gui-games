"""taking into account dynamic shaping"""

from turtle import Screen
from tetris_shape import Shape

BGCOLOR = "black"
PLAYABLE_AREA = "orange"


class Window:
    """docs"""

    count = 0

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
        self.reset_previous_grid_row()
        for y, lst in enumerate((shape.block)):
            for x, value in enumerate(lst):
                self.grid[row + y][col + x] = value
        self.starting_row += 1
        print(f"{Window.count}. Placed\n{self.pretty_grid()}")

    def reset_previous_grid_row(self):
        """Grid upper rows value set to 0"""
        if self.starting_row - 1 < 0:
            return
        row = self.starting_row - 1
        self.grid[row] = [0 for _ in range(12)]
        print(f"{Window.count}. Reseted\n{self.pretty_grid()}")

    def draw_grid(self, shape: Shape):
        """Put shape in in center of length and starts convert
        0s to 1s according given Shape"""
        column = self.start_in_column(shape=shape)
        # put shape values into grid
        self.place_matrix_value(row=self.starting_row, col=column, shape=shape)

    def is_under_the_shape_bottom_block_empty(self, shape: Shape):
        """_summary_"""
        # If Shape last row elements are all 0s and there is still sapace to go down
        if (shape.height - 1) + self.starting_row > len(self.grid) - 1:
            return False
        if (shape.height - 1) + self.starting_row == len(self.grid) - 1:
            return self.grid[self.starting_row + 1][
                self.starting_col : self.starting_col + shape.width
            ] == [0 for _ in range(shape.width)]

        return self.grid[(shape.height - 1) + self.starting_row][
            self.starting_col : self.starting_col + shape.width
        ] == [0 for _ in range(shape.width)]

    # def is_shape_height_fit_in_bottom_area(self, shape: Shape):
    #     """Shape area can be fitted if it moved"""
    #     return len(self.grid) - self.starting_row >= shape.height

    def move_down(self, shape: Shape):
        """Updates starting point value according height of shape"""
        # shape_bottom_area = shape.shape_bottom_list_len()
        if self.starting_row == len(self.grid) - 1:
            return
        # if not self.is_shape_height_fit_in_bottom_area(shape=shape):
        #     return
        if not self.is_under_the_shape_bottom_block_empty(shape=shape):
            return
        self.place_matrix_value(
            row=self.starting_row, col=self.starting_col, shape=shape
        )

    def pretty_grid(self):
        """docs"""
        Window.count += 1
        map_grid = map(lambda item: f"{item[0]}. {item[1]}", enumerate(self.grid))
        return "\n".join(map_grid)


def place_shape():
    """docs"""
    block = Shape()
    block.create_specific_shape("z")
    # pprint(block.block)
    window = Window(width=600, height=800)
    # print(f"New grid start row index: {window.starting_row}")
    window.draw_grid(shape=block)
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
    # print(f"Last view\n{window.pretty_grid()}")


place_shape()
