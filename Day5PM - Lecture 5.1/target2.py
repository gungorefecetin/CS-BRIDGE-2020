"""
File: target.py
---------------
This program draws a red and white target symbol in the center of the screen.
"""

from graphics import Canvas


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Target")

    height = canvas.get_canvas_height()
    width = canvas.get_canvas_width()

    _height = height / 2
    _width = width / 2

    radius = 245  # I've tested it, 245 is the max radius. You can change it but be sure the radius <= 245

    num_of_iterations = 13

    for i in range(num_of_iterations):
        circle = canvas.create_oval(_width - radius, _height - radius, _width + radius,
                                    _height + radius)

        radius -= 20

        if i % 2 == 0:
            canvas.set_fill_color(circle, 'red')
        else:
            canvas.set_fill_color(circle, 'white')

    canvas.mainloop()


if __name__ == '__main__':
    main()
