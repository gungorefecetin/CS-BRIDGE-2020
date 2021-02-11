"""
File: making_tracks.py
-------------------
This program draws a track wherever the user clicks the mouse.
"""

from graphics import Canvas


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Making Tracks")

    # TODO: your code here!

    while True:
        clicks = canvas.get_new_mouse_clicks()

        for click in clicks:
            load_image(click.x, click.y, canvas)
        canvas.update()

    canvas.mainloop()


def load_image(coordinatex, coordinatey, canvas):
    return canvas.create_image(coordinatex, coordinatey, "images/simba-sm.jpg")


if __name__ == '__main__':
    main()
