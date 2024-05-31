"""List of Turtles Paddle to get prices distance value"""

from turtle import Turtle
from random import choice

MOVE_BY = 20


class Paddles:
    """A class that represents a paddle in the breakout game.

    Attributes:
        segments (list): A list of turtle segments that make up the paddle.
        colors (list): A list of colors for the paddle segments.
        default_positions (list): A list of default positions for the paddle segments.

    Args:
        positions (list): The default positions where the segments should be added.
    """

    def __init__(self, positions):
        self.segments = []
        self.colors = ["red", "blue", "green", "yellow", "purple"]
        self.default_positions = positions
        self.initiliazer()

    def add_segments(self, position, color=None):
        """Add a segment to the paddle.

        Args:
            position (tuple): The position where the segment should be added.
            color (str, optional): The color of the segment. If not provided, a random color will be chosen.
        """
        if color is None:
            color = choice(self.colors)
        if self.colors:
            segment = Turtle(shape="square")
            segment.penup()
            segment.color(color)
            segment.shapesize(stretch_len=1)
            segment.goto(position)
            self.segments.append(segment)
        else:
            self.colors = ["red", "blue", "green", "yellow", "purple"]

    def initiliazer(self):
        """Initialize the paddle by adding segments to the default positions."""
        for i, position in enumerate(self.default_positions):
            self.add_segments(position, self.colors[i])

    def go_right(self, boundary):
        """Move the paddle to the right.

        Args:
            boundary (int): The right boundary of the game screen.
        """
        head = self.segments[-1]
        head.setheading(0)
        if head.xcor() + 20 < boundary:
            for i in range(len(self.segments) - 1):
                new_x = self.segments[i + 1].xcor()
                new_y = self.segments[i + 1].ycor()
                self.segments[i].goto(new_x, new_y)
            head.forward(MOVE_BY)

    def go_left(self, boundary):
        """Move the paddle to the left.

        Args:
            boundary (int): The left boundary of the game screen.
        """
        head = self.segments[0]
        head.setheading(180)
        if head.xcor() - 20 > -boundary:
            for i in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[i - 1].xcor()
                new_y = self.segments[i - 1].ycor()
                self.segments[i].goto(new_x, new_y)
            head.forward(MOVE_BY)

    def extend(self):
        """Extend the paddle by adding a new segment."""
        if self.colors and len(self.segments) < 10:
            color = self.colors.pop()
            self.add_segments(self.segments[-1].position(), color=color)

    def shrink(self):
        """Shrink the paddle by removing the last segment."""
        if len(self.segments) > 5:
            segment = self.segments.pop()
            segment.goto(0, -500)
            segment.color("black")
            del segment
