"""TV Approach
Usage of Matrix where 1s for turtle stamp."""

import random

COLORS = ["red", "blue", "yellow", "lightblue", "purple"]

blocks = {
    "cube": [[1, 1, 1] for _ in range(3)],
    "line": [[1 for _ in range(4)]],
    "t": [[1, 1, 1], [0, 1, 0]],
    "z": [[1, 1, 0], [0, 1, 0], [0, 1, 1]],
    "L": [[1, 1, 1], [0, 0, 1]],
}


class Shape:
    """Every call choose matrix randomly, size effects width and height of shape
    Turtle(shape='square') by default width and height is 1 covers 20 pixel ares"""

    def __init__(self) -> None:
        self.block = random.choice(list(blocks.values()))
        self.height = len(self.block)
        self.width = len(self.block[0])
        self.color = random.randint(1, 5)
        self.active = True

    def shape_bottom_list_len(self):
        """Calculates and returns last matrix of shape len"""
        return len(self.block[-1])

    def create_specific_shape(self, shape_name):
        """For test purpose get cube matrix"""
        self.block = blocks[shape_name]
        self.height = len(self.block)
        self.width = len(self.block[0])

    def transpose_the_matrix(self):
        """Convert rows to columns, columns to rows
        list of list to list of tuple and updates
        new order matrix of block"""
        self.block = list(zip(*self.block))

    def clockwise(self):
        """Rotate by horizontally"""
        self.transpose_the_matrix()
        self.block = [list(reversed(row)) for row in self.block]

    def anti_clockwise(self):
        """Rotate by vertically"""
        self.transpose_the_matrix()
        self.block = [list(row) for row in reversed(self.block)]
