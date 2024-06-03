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
shape.create_specific_shape("t")

scr.window.onkey(lambda: scr.move_left(shape), "Left")
scr.window.onkey(lambda: scr.move_right(shape), "Right")


scr.start_in_column(shape=shape)
stamp.draw_grid(width=WIDTH, height=HEIGHT, shape=shape, grid=scr.grid)

while True:
    scr.window.update()

    scr.move_down(shape=shape)
    stamp.draw_grid(width=WIDTH, height=HEIGHT, shape=shape, grid=scr.grid)


scr.window.mainloop()
