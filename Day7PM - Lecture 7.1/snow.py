"""
File: snow.py
-------------
Animates snow falling from the top to the bottom of the screen.  Snowflakes will be randomly added at the top at
random locations, and animated downwards together until they reach the bottom of the screen.
"""

from graphics import Canvas
import random
import time

ANIMATION_DELAY_SECONDS = 0.01
SNOWFLAKE_DIAMETER = 10


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Snow")

    SNOWS = []

    while True:
        coordinatex = random.randint(0, canvas.get_canvas_width() - SNOWFLAKE_DIAMETER)
        coordinatey = 0

        prob = random.choice([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])

        if prob:
            SNOWS.append(make_snow(coordinatex, coordinatey, canvas))

        for snow in SNOWS:
            snow_fall(snow, 0, 5, canvas)

        canvas.update()
        time.sleep(ANIMATION_DELAY_SECONDS)

    canvas.mainloop()


def make_snow(coordinatex, coordinatey, canvas):
    snow = canvas.create_oval(coordinatex, coordinatey,
                              coordinatex + SNOWFLAKE_DIAMETER,
                              coordinatey + SNOWFLAKE_DIAMETER)

    canvas.set_fill_color(snow, 'black')

    return snow


def snow_fall(snow, dx, dy, canvas):

    if not canvas.get_top_y(snow) + SNOWFLAKE_DIAMETER >= canvas.get_canvas_height():
        canvas.move(snow, dx, dy)


if __name__ == '__main__':
    main()
