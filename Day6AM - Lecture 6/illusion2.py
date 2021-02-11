"""File: illusion2.py
------------------------
This program draws an optical illusion of an off-checkerboard pattern.
"""

from graphics import Canvas

# These constants tell the graphics canvas how big to be.  You can ignore them.
# Use get_canvas_width() and get_canvas_height() instead.
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500

# The height of each row, and the size of each square. use this!
SQUARE_SIZE = 50

# The number of rows.  Use this!
NUM_ROWS = 10


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("Illusion 2")

    for row in range(NUM_ROWS):
        draw_square(canvas, row)

    canvas.mainloop()


def draw_square(canvas, row):
    for i in range(CANVAS_WIDTH // SQUARE_SIZE):
        if row % 4 == 0:
            n = 0
        elif row % 2 == 0:
            n = 0.5
        else:
            n = 0.25
        rec = canvas.create_rectangle(i * SQUARE_SIZE + n*SQUARE_SIZE, row * SQUARE_SIZE, (i + 1) * SQUARE_SIZE + n*SQUARE_SIZE,
                                      (row + 1) * SQUARE_SIZE)
        if i % 2 == 0:
            canvas.set_color(rec, "black")


if __name__ == '__main__':
    main()
