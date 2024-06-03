"""Painting Part"""

from tetris_screen import Window
from tetris_shape import Shape
from tetris_stamp import Stamp


WIDTH = 600
HEIGHT = 800


scr = Window(width=WIDTH, height=HEIGHT)
scr.window.tracer(0)

scr.window.listen()

stamp = Stamp()
shape = Shape()
shape.create_specific_shape("z")


scr.window.onkey(lambda: scr.move_left(shape), "Left")
scr.window.onkey(lambda: scr.move_right(shape), "Right")
scr.window.onkey(shape.clockwise, "Up")
scr.window.onkey(shape.anti_clockwise, "Down")


scr.starting_coordinates(shape=shape)
stamp.draw_screen(width=WIDTH, height=HEIGHT, grid=scr.grid)


while True:
    scr.window.update()

    if not shape.active:
        shape = Shape()

        scr.starting_coordinates(shape=shape)
    scr.move_down(shape=shape)

    stamp.draw_screen(width=WIDTH, height=HEIGHT, grid=scr.grid)


scr.window.mainloop()
