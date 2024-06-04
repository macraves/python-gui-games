# Noteworthy Notes in the Game Repository:

## Tetris Game

For the Tetris game, the recorded git log entries provided a good reference for listing programming mistakes. Upon further research, I discovered that applying the working principle of TV screens would reduce computational load. Before proceeding with this approach, I tried two different methods:

- Initially, I wanted to use four different turtle objects for each square of the blocks in a 2x2 2D list. A block consisting of four adjacent squares would mean 16 turtle objects on a 4x4 grid. This would create unnecessary memory load, and I realized it could lead to a time complexity of more than n^2 \* n^2 for clearing the blocks, so I abandoned this idea.
- My second idea was to change the turtle size variable and draw the blocks using a single turtle. However, in this approach, the turtle would move down along with the blocks, covering unnecessary distances. At this point, I started researching to better understand the game mechanics.

### Conclusion

In graphic design, it is crucial to understand the working principles and draft a blueprint accordingly. Due to the slowdown caused by the Turtle module (Consider pre-rendering blocks or using an alternative graphical library like Pygame for better performance), the program was developed solely to place blocks correctly, without adding score and other features.
