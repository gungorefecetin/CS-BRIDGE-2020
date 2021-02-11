"""
File: mouse_location.py
-------------------
This program displays a label in the center of the screen displaying the current mouse coordinates.
"""

from graphics import Canvas


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Mouse Location")

    # TODO: your code here!

    while True:
        coordinatex = canvas.get_mouse_x()
        coordinatey = canvas.get_mouse_y()

        coordinates = '(' + str(coordinatex) + ', ' + str(coordinatey) + ')'

        text = canvas.create_text(canvas.get_canvas_width() / 2, canvas.get_canvas_height() / 2, coordinates)
        canvas.set_font(text, 'Courier', 30)

        canvas.update()

        canvas.delete(text)

    canvas.mainloop()


if __name__ == "__main__":
    main()
