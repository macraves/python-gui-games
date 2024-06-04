"""Painting Part"""

# import time
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
TEST_SHAPE = "cube"
# shape.create_specific_shape(TEST_SHAPE)

scr.window.onkey(lambda: scr.move_left(shape), "Left")
scr.window.onkey(lambda: scr.move_right(shape), "Right")
scr.window.onkey(lambda: scr.clockwise(shape), "Up")
scr.window.onkey(lambda: scr.anti_clockwise(shape), "Down")


scr.starting_coordinates(shape=shape)
stamp.draw_screen(width=WIDTH, height=HEIGHT, grid=scr.grid)


while True:
    scr.window.update()
    if not shape.active:
        shape = Shape()
        # shape.create_specific_shape(TEST_SHAPE)
        scr.starting_coordinates(shape=shape)

    scr.move_down(shape=shape)

    stamp.draw_screen(width=WIDTH, height=HEIGHT, grid=scr.grid)
    # time.sleep(0.5 * 0.6)


scr.window.mainloop()
