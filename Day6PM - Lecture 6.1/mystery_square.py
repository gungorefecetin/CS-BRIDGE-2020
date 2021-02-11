"""
File: mystery_square.py
-------------------
This program creates a centered square that changes color randomly every second.
"""

from graphics import Canvas

# Needed for pausing for animation.  Don't remove this.
import time
import random

# Size of the centered square
SQUARE_SIZE = 400

# Delay between color changes, in seconds
DELAY = 1


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Mystery Square")

    width = canvas.get_canvas_width()
    height = canvas.get_canvas_height()

    _width = width / 2
    _height = height / 2

    # TODO: your code here

    square = canvas.create_rectangle(_width - SQUARE_SIZE // 2, _height - SQUARE_SIZE // 2, _width + SQUARE_SIZE // 2,
                                     _height + SQUARE_SIZE // 2)

    while True:
        num = random.randint(0, len(canvas.COLORS) - 1)
        canvas.set_fill_color(square, canvas.COLORS[num])
        canvas.set_outline_color(square, canvas.COLORS[num])
        canvas.update()
        time.sleep(DELAY)

    canvas.mainloop()


if __name__ == "__main__":
    main()
