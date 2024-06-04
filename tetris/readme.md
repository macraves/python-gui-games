# Tetris Game

This is a simple implementation of the classic Tetris game using Python and the Turtle graphics library. The game focuses on block placement and movement, with future plans to add scoring and other features.

## Files

- **`tetris_shape.py`**: Contains the `Shape` class which handles the creation and manipulation of Tetris blocks.
- **`tetris_stamp.py`**: Contains the `Stamp` class which is responsible for drawing the Tetris grid and blocks on the screen using the Turtle graphics library.
- **`tetris_screen.py`**: Contains the `Window` class which handles the game screen, block placement, and game logic.
- **`main.py`**: The main entry point of the game which sets up the game window, listens for user inputs, and runs the game loop.

## `tetris_shape.py`

This file defines the `Shape` class, which represents the Tetris blocks. It includes:

- A dictionary of block shapes.
- Methods to initialize a shape, replace numbers with color codes, calculate the height and width, and rotate the shapes both clockwise and anti-clockwise.

## `tetris_stamp.py`

This file defines the `Stamp` class, a subclass of `Turtle`, which handles the drawing of the game grid and blocks. It includes:

- Initialization of the turtle.
- Method to draw the game grid on the screen.

## `tetris_screen.py`

This file defines the `Window` class, which manages the game window and logic. It includes:

- Initialization of the game window.
- Methods to check and clear full rows, calculate starting coordinates, place and remove shapes, and move shapes left, right, and down.
- Methods to rotate shapes clockwise and anti-clockwise.
- The direction of the shape (left, right) needs optimization
- A method to generate a pretty-printed version of the game grid for debugging.

## `main.py`

This file is the main entry point of the game. It sets up the game window, listens for user inputs, and runs the game loop. It includes:

- Initialization of the game window and grid.
- Key bindings for moving and rotating shapes.
- The game loop, which updates the game state and redraws the grid.

## How to Run

1. Make sure you have Python installed on your system.
2. Run `main.py` using the following command:

   ```bash
   python main.py
   ```

## Future Enhancements

- Implement scoring and level progression.
- Add more features like pause/resume, game over screen, and high score tracking.
- Optimize performance by minimizing turtle movements and considering alternative graphical libraries.

## Acknowledgements

This Tetris game was created for educational purposes, to learn and apply concepts of game development using Python and the Turtle graphics library.
