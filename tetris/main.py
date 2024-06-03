"""Painting Part"""

from tetris_screen import Window
from tetris_shape import Shape
from tetris_stamp import Stamp


WIDTH = 600
HEIGHT = 800


scr = Window(width=WIDTH, height=HEIGHT)
shape = Shape()
shape.create_specific_shape("t")
stamp = Stamp()
scr.set_middle_of_the_screen(shape=shape)
scr.window.tracer(0)

stamp.draw_grid(width=WIDTH, height=HEIGHT, shape=shape, grid=scr.grid)
while True:
    scr.window.update()
    scr.move_down(shape=shape)
    stamp.draw_grid(width=WIDTH, height=HEIGHT, shape=shape, grid=scr.grid)


scr.window.mainloop()
