"""
File: illusion1.py
------------------------
This program draws an optical illusion of a checkerboard pattern.
"""

from graphics import Canvas


# These constants tell the graphics canvas how big to be.  You can ignore them.
# Use get_canvas_width() and get_canvas_height() instead.

CANVAS_WIDTH = 540
CANVAS_HEIGHT = 430

# The size of each dimension of the square. use this!
SIZE = 100

# The space between two squares. Use this!
GAP = 10


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("Illusion 1")

    for x in range(CANVAS_WIDTH // SIZE):
        for y in range(CANVAS_HEIGHT // SIZE):
            draw_square(canvas, x, y)

    canvas.mainloop()


def draw_square(canvas, x, y):
    square = canvas.create_rectangle(x * SIZE + (x * GAP), y * SIZE + (y * GAP), (x+1) * SIZE + (x * GAP), (y+1) * SIZE + (y * GAP))

    canvas.set_color(square, 'black')


if __name__ == '__main__':
    main()
