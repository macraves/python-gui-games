"""taking into account dynamic shaping"""

from turtle import Screen
from tetris_shape import Shape

BGCOLOR = "black"
# PLAYABLE_AREA = "orange"
HEIGHT = 16
WIDTH = 12


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
        self.grid = [[0] * WIDTH for _ in range(HEIGHT)]
        self.starting_row = 0
        self.starting_col = 0

    def check_row_is_full(self):
        """docs"""
        for i, row in enumerate(self.grid):
            if all(num != 0 for num in row):
                self.grid[i] = [0] * WIDTH
                for j in range(i, 0, -1):
                    self.grid[j], self.grid[j - 1] = self.grid[j - 1], self.grid[j]

    def starting_coordinates(self, shape: Shape):
        """Calculate grid width to place Shape in the middle of the screen"""
        self.starting_row = 0
        half_screen_width = len(self.grid[0]) // 2
        half_shape_width = shape.shape_width() // 2
        column = half_screen_width - half_shape_width - 1
        self.starting_col = column

    def place_matrix_value(self, row, col, shape: Shape):
        """docs"""

        for y, lst in enumerate((shape.block)):
            # self.grid[row + y][col : col + shape.shape_width()] = lst
            for x, value in enumerate(lst):
                if not value:
                    continue
                if self.grid[row + y][col + x] == 0:
                    self.grid[row + y][col + x] = value
                # elif self.grid[row + y][col+x] != 0:
        if Window.flag:
            print(f"{Window.count}. Placed\n{self.pretty_grid()}")

    def reset_the_bellow_row(self, shape: Shape):
        """docs"""
        if self.starting_row - 1 < 0:
            return
        previous_row = self.starting_row - 1
        self.grid[previous_row][
            self.starting_col : self.starting_col + shape.shape_width()
        ] = [0] * (shape.shape_width())
        if Window.flag:
            print(f"{Window.count}. Reseted\n{self.pretty_grid()}")

    def remove_shape_code(self, shape: Shape):
        """docs"""
        if self.starting_row - 1 < 0:
            return
        row_to_check = self.starting_row - 1
        col_to_start = self.starting_col
        for y, row in enumerate(shape.block):
            for x, value in enumerate(row):
                if not value:
                    continue
                if self.grid[y + row_to_check][x + col_to_start] == value:
                    self.grid[y + row_to_check][x + col_to_start] = 0
        # for y, _ in enumerate(shape.block):
        #     till = col_to_start + shape.shape_width()
        #     self.grid[y + row_to_check][col_to_start:till] = [0] * (till - col_to_start)

        if Window.flag:
            print(f"{Window.count}. Removed\n{self.pretty_grid()}")

    def does_the_bottom_of_the_shape_fit_on_the_line_below(self, row, shape: Shape):
        """_summary_"""
        shape_bottom_row_len = shape.shape_bottom_list_len()
        return (
            self.grid[row][self.starting_col : self.starting_col + shape_bottom_row_len]
            == [0] * shape_bottom_row_len
        )

    def does_shape_width_fit_next_row(self, shape):
        """docs"""
        next_row = self.starting_row + shape.shape_height() - 1
        if next_row > len(self.grid) - 1:
            return False
        if not self.does_the_bottom_of_the_shape_fit_on_the_line_below(
            row=next_row, shape=shape
        ):
            return False
        return (
            self.grid[next_row][
                self.starting_col : self.starting_col + shape.shape_width()
            ]
            == [0] * shape.shape_width()
        )

    def can_shape_move_down(self, shape: Shape):
        """docs"""
        shape_height = shape.shape_height()
        current_row_index = self.starting_row
        boundry = len(self.grid)
        # Check if Current row index is out of boundry
        if current_row_index > boundry:
            return False
        # Check if current index + height is in the grid boundry
        if current_row_index + shape_height > len(self.grid):
            return False
        # Check shape color codes match with grid 0s
        self.remove_shape_code(shape=shape)
        for y, row in enumerate(shape.block):
            for x, value in enumerate(row):
                if value:
                    if self.grid[current_row_index + y][self.starting_col + x] != 0:
                        return False
        return True

    def move_down(self, shape: Shape):
        """Updates starting point value according height of shape"""

        if self.can_shape_move_down(shape=shape):
            self.place_matrix_value(
                row=self.starting_row, col=self.starting_col, shape=shape
            )
            self.starting_row += 1
        else:
            self.place_matrix_value(
                row=self.starting_row - 1, col=self.starting_col, shape=shape
            )
            shape.active = False
            self.check_row_is_full()

    def move_left(self, shape: Shape):
        """Set column -1"""
        if not shape.active:
            return
        if self.starting_col <= 0:
            return
        self.remove_shape_code(shape=shape)
        self.starting_col -= 1

    def move_right(self, shape: Shape):
        """Set column -1"""
        if not shape.active:
            return
        if self.starting_col + shape.shape_width() >= len(self.grid[0]):
            return
        self.remove_shape_code(shape=shape)
        self.starting_col += 1

    def clockwise(self, shape: Shape):
        """Rotate by horizontally"""
        if not shape.active:
            return
        self.remove_shape_code(shape=shape)
        shape.clockwise()

    def anti_clockwise(self, shape: Shape):
        """Rotate by vertically"""
        if not shape.active:
            return
        self.remove_shape_code(shape=shape)
        shape.anti_clockwise()

    def pretty_grid(self):
        """docs"""
        Window.count += 1
        # sample = self.grid[:10]
        sample = self.grid
        if Window.flag:
            return "\n".join(f"{item[0]:02}. {item[1]}" for item in enumerate(sample))

    def test_window(self, block):
        """docs"""
        block = Shape()

        block.create_specific_shape("cube")
        self.starting_coordinates(block)
        # pprint(block.block)
        # window = Window(width=600, height=800)
        # print(f"New grid start row index: {window.starting_row}")

        # while block.active:
        #     self.move_down(shape=block)
        # self.clockwise(block)

        # print(window.pretty_grid())
        # print(f"New grid current row index: {window.starting_row}")
        while self.can_shape_move_down(block):
            self.move_down(shape=block)

        # self.move_down(shape=block)
        # self.clockwise(block)
        # print(f"New grid current row index: {window.starting_row}")


def test_main():
    """docs"""
    scr = Window(width=600, height=800)
    design = Shape()
    scr.test_window(design)


# test_main()
