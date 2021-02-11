"""
File: short_film.py
----------------
Creates a short animated film with a sunset to start off with.
"""

from graphics import Canvas
import time

SUN_RADIUS = 25

# The amount the sun should move down the screen each frame
DESCENT = 2

# in seconds
DELAY = 0.03

CANVAS_WIDTH = 754
CANVAS_HEIGHT = 492


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Short Film")

    # FILM BEGINS...

    display_message(canvas, 'Once upon a time...')
    create_air_and_ground(canvas)
    sun = create_sun(canvas)
    get_sun_color(canvas, sun)

    # FILM ENDS...

    display_message(canvas, 'The end...')


def display_message(canvas, message):
    canvas.set_canvas_background_color('black')

    label = canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, message)
    canvas.set_font(label, 'Times New Roman', 40)
    canvas.set_fill_color(label, 'white')

    canvas.update()
    time.sleep(2)

    canvas.delete(label)


def create_air_and_ground(canvas):
    air = canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT // 2)
    canvas.set_fill_color(air, 'blue')

    ground = canvas.create_rectangle(0, CANVAS_HEIGHT // 2, CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_fill_color(ground, 'lime green')


def create_sun(canvas):
    sun = canvas.create_oval(CANVAS_WIDTH / 2 - SUN_RADIUS, CANVAS_HEIGHT / 4 - SUN_RADIUS,
                             CANVAS_WIDTH / 2 + SUN_RADIUS,
                             CANVAS_HEIGHT / 4 + SUN_RADIUS)

    canvas.set_fill_color(sun, 'yellow')

    return sun


def get_sun_color(canvas, sun):
    while True:
        if canvas.get_top_y(sun) >= CANVAS_HEIGHT / 2 - SUN_RADIUS * 2:
            canvas.set_fill_color(sun, 'orange')

        if canvas.get_top_y(sun) >= CANVAS_HEIGHT / 2 - SUN_RADIUS:
            canvas.set_fill_color(sun, 'red')

        if canvas.get_top_y(sun) >= CANVAS_HEIGHT / 2:
            air = canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT // 2)
            canvas.set_fill_color(air, 'black')

            ground = canvas.create_rectangle(0, CANVAS_HEIGHT / 2, CANVAS_WIDTH, CANVAS_HEIGHT)
            canvas.set_fill_color(ground, 'black')
            break

        canvas.move(sun, 0, DESCENT)

        ground = canvas.create_rectangle(0, CANVAS_HEIGHT / 2, CANVAS_WIDTH, CANVAS_HEIGHT)
        canvas.set_fill_color(ground, 'green')

        canvas.update()
        time.sleep(DELAY)


if __name__ == '__main__':
    main()
