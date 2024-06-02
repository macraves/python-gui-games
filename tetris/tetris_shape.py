"""TV Approach
Usage of Matrix where 1s for turtle stamp."""

import random

blocks = {
    "square": [[1, 1, 1] for _ in range(3)],
    "line": [[1 for _ in range(4)]],
    "t": [[1, 1, 1], [0, 1, 0], [0, 0, 0]],
    "z": [[1, 1, 0], [0, 1, 0], [0, 1, 1]],
}


class Shape:
    """Every call choose matrix randomly, size effects width and height of shape
    Turtle(shape='square') by default width and height is 1 covers 20 pixel ares"""

    def __init__(self) -> None:
        self.shape = random.choice(list(blocks.values()))
        self.height = len(self.shape)
        self.width = len(self.shape[0])

    def transpose_the_matrix(self):
        """Convert rows to columns, columns to rows
        list of list to list of tuple"""
        self.shape = list(zip(*self.shape))

    def clockwise(self):
        """Rotate by horizontally"""
        self.transpose_the_matrix()
        self.shape = [list(reversed(row)) for row in self.shape]

    def anti_clockwise(self):
        """Rotate by vertically"""
        self.transpose_the_matrix()
        self.shape = [list(row) for row in reversed(self.shape)]
