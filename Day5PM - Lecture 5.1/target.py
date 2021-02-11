"""
File: target.py
---------------
This program draws a red and white target symbol in the center of the screen.
"""

from graphics import Canvas

# The sizes of the concentric circles
BIG_CIRCLE_RADIUS = 150
MEDIUM_CIRCLE_RADIUS = 100
SMALL_CIRCLE_RADIUS = 50


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Target")

    height = canvas.get_canvas_height()
    width = canvas.get_canvas_width()

    _height = height / 2
    _width = width / 2

    big_circle = canvas.create_oval(_width - BIG_CIRCLE_RADIUS, _height - BIG_CIRCLE_RADIUS, _width + BIG_CIRCLE_RADIUS,
                                    _height + BIG_CIRCLE_RADIUS)

    medium_circle = canvas.create_oval(_width - MEDIUM_CIRCLE_RADIUS, _height - MEDIUM_CIRCLE_RADIUS,
                                       _width + MEDIUM_CIRCLE_RADIUS, _height + MEDIUM_CIRCLE_RADIUS)

    small_circle = canvas.create_oval(_width - SMALL_CIRCLE_RADIUS, _height - SMALL_CIRCLE_RADIUS,
                                      _width + SMALL_CIRCLE_RADIUS, _height + SMALL_CIRCLE_RADIUS)

    canvas.set_fill_color(big_circle, 'red')
    canvas.set_fill_color(medium_circle, 'white')
    canvas.set_fill_color(small_circle, 'red')

    canvas.mainloop()


if __name__ == '__main__':
    main()
