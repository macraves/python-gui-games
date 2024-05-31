"""test workbench
-window boundry
-snap shot
-distance"""

from turtle import Turtle


class Border(Turtle):
    """docs"""

    def __init__(self):
        super().__init__()
        self.color("white")

    def default_setheading(self):
        """docs"""
        self.setheading(0)

    def bottom_line(self, width, height, pad_bottom):
        """docs"""
        self.penup()
        self.default_setheading()
        self.goto(-(width // 2), -((height // 2) - pad_bottom))
        self.pendown()
        self.forward(width)

    def upper_line(self, width, height, pad_upper):
        """docs"""
        self.penup()
        self.default_setheading()
        self.goto(-(width // 2), ((height // 2) - pad_upper))
        self.pendown()
        self.forward(width)

    def left_line(self, width, height, pad_sides, pad_bottom, pad_upper):
        """docs"""
        self.penup()
        self.default_setheading()
        self.goto(-((width // 2) - pad_sides), -((height // 2) - (pad_bottom)))
        self.left(90)
        self.pendown()
        self.forward(height - (pad_bottom + pad_upper))

    def right_line(self, width, height, pad_upper, pad_bottom, pad_sides):
        """docs"""
        self.penup()
        self.default_setheading()
        self.goto(((width // 2) - pad_sides), -((height // 2) - (pad_bottom)))
        self.left(90)
        self.pendown()
        self.forward(height - (pad_bottom + pad_upper))


def draw_borders(width, height, pad_upper, pad_bottom, pad_sides):
    """docs"""
    pen = Border()
    pen.bottom_line(width=width, height=height, pad_bottom=pad_bottom)
    pen.right_line(
        width=width,
        height=height,
        pad_upper=pad_upper,
        pad_bottom=pad_bottom,
        pad_sides=pad_sides,
    )
    pen.left_line(
        width=width,
        height=height,
        pad_sides=pad_sides,
        pad_bottom=pad_bottom,
        pad_upper=pad_upper,
    )
    pen.upper_line(width=width, height=height, pad_upper=pad_upper)


def place_ball_to_position(postion, count, color, cls_ball, top, board):
    """docs"""
    x_cor, y_cor = postion
    up_value = 25
    the_ball = cls_ball()
    the_ball.color(color)
    the_ball.goto(x_cor, y_cor + up_value)
    for i, segment in enumerate(board.segments):
        print(
            f"{count}. {color} ball distance to {i} "
            f"segment {segment.color()} {top.distance(segment)}"
        )


def snap_shot(current_ball: Turtle, cls_ball):
    """docs"""
    x_cor, y_cor = current_ball.xcor(), current_ball.ycor()
    the_ball = cls_ball()
    the_ball.goto(x_cor, y_cor)


def test_ball_with_segments(board, cls_ball):
    """docs"""
    segments = board.segments
    test_segment = segments[0]
    test_segment_positon = segments[0].position()
    x_cor, y_cor = test_segment_positon
    the_ball = cls_ball()
    the_ball.color(test_segment.color()[0])
    the_ball.goto(x_cor, y_cor + 25)

    for i, segment in enumerate(segments):
        print(
            f"Ball distance from {i}.segment {segment.color()[0]}: {the_ball.distance(segment)}"
        )
