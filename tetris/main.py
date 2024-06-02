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

stamp.draw_grid(width=WIDTH, height=HEIGHT, shape=shape, grid=scr.grid)


scr.window.mainloop()
