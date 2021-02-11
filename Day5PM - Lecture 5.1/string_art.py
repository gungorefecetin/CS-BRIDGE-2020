"""
File: string_art.py
-------------------
This program creates string art using only straight lines.
"""

from graphics import Canvas

# Size of the canvas
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

# The number of pixels between end points of each line
LINE_SPACING = 20

# The number of lines we will have to draw
NUM_LINES = CANVAS_WIDTH // LINE_SPACING


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("String Art")

    height = canvas.get_canvas_height()

    for i in range(1, NUM_LINES+1):
        a = i * LINE_SPACING

        x1 = a
        y2 = a

        canvas.create_line(x1, height, 0, y2)

    canvas.mainloop()


if __name__ == "__main__":
    main()
