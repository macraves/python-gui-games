"""Shape in tetris"""

from grid_lines import Square

SHAPES = """
[x,y][x+z,y][x+2z,y][x+3z,y]

# Second option
       [x ,y+z]
[x-z, y][x, y][x+z, y]

[x-z y+z][x,    y+z][x+z,  y]
[x-z,  y][x,      y][x+z,  y]
[x-z,y-z][x    ,y-z][x+z,y-z]
"""

MATRIX = {"line": []}


class Shape:
    """docs"""

    def __init__(self):
        self.starting_point = Square.starting_point
        self.colors = ["red", "blue", "green", "yellow"]
        self.create_line()
        # self.create_cube()
        # self.create_t_shape()

    def width_and_hight(self):
        """docs"""
        suquare = Square()
        return suquare.get_distance()

    def create_line(self):
        """docs"""
        line = []
        for i in range(4):
            blocks = Square()
            print(blocks.starting_point)
            blocks.squares = [square.color(self.colors[i]) for square in blocks.squares]
            width, _ = blocks.get_distance()
            x_cor, y_cor = Square.starting_point
            Square.starting_point = (x_cor + width), y_cor
            line.append(blocks)
        Square.starting_point = self.starting_point

    def create_cube(self):
        """docs"""
        cube = []
        colors = self.colors * 3
        width, height = self.width_and_hight()
        center = self.starting_point
        coordinates = [
            (center[0] + width * x, center[1] - height * y)
            for y in range(3)
            for x in range(3)
        ]
        for i, coordinate in enumerate(coordinates):
            Square.starting_point = coordinate
            blocks = Square()
            blocks.squares = [block.color(colors[i]) for block in blocks.squares]
            cube.append(blocks)
        Square.starting_point = self.starting_point

    def create_t_shape(self):
        """docs"""
        t_shape = []
        width, height = self.width_and_hight()
        center = self.starting_point
        coordinates = [(center[0] + width * x, center[1]) for x in range(3)]
        coordinates.append(
            (self.starting_point[0] + width, self.starting_point[1] + height)
        )
        for origin in coordinates:
            Square.starting_point = origin
            blocks = Square()
            t_shape.append(blocks)
        Square.starting_point = self.starting_point


#     [x+z ,y+z]
# [x, y][x+z, y][x, y]


#       [x+z, y+z]
#       [x+z, y][x+2z, y]
#       [x-z, y-z]


#        [x+z ,y+z]
# [x,    y][x+z, y]
#         [x+z, y-z]

# [x,y][x+z,y][x+2z,y][x+3z,y]

# [x,y]
# [x, y-z]
# [x, y-2z]
# [x, y-3z]
