"""
File: catch_me_if_you_can.py
-------------------
This program draws several black "distractor" squares on the screen, along with a blue square that the user
tries to touch with their mouse.  But whenever the mouse touches the blue square, it moves to
another new random location!
"""

from graphics import Canvas
import random

# The dimensions of each black distractor square
DISTRACTOR_SIZE = 50

# The number of black squares on screen
N_DISTRACTORS = 20

# The dimensions of the blue square the user is trying to touch with the mouse
GOAL_SIZE = 60


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Catch Me If You Can")

    diss = create_dis(canvas)
    sneaky = create_sneaky(canvas)
    finished = False

    while not finished:
        clicks = canvas.get_new_mouse_clicks()
        for i in clicks:
            finished = hit(canvas, i, sneaky)
            if not finished:
                sneaky = recreate_game(canvas, diss, sneaky)
        canvas.update()


    canvas.mainloop()


def create_sneaky(canvas):
    x = random.randint(0, canvas.get_canvas_width() - GOAL_SIZE)
    y = random.randint(0, canvas.get_canvas_height() - GOAL_SIZE)

    sneaky = canvas.create_rectangle(x, y, x + GOAL_SIZE, y + GOAL_SIZE)
    canvas.set_color(sneaky, "blue")
    return sneaky


def create_dis(canvas):
    diss = []
    for i in range(N_DISTRACTORS):
        x = random.randint(0, canvas.get_canvas_width() - DISTRACTOR_SIZE)
        y = random.randint(0, canvas.get_canvas_height() - DISTRACTOR_SIZE)
        DIS = canvas.create_rectangle(x, y, x + DISTRACTOR_SIZE, y + DISTRACTOR_SIZE)
        canvas.set_color(DIS, "black")
        diss.append((x, y, x + DISTRACTOR_SIZE, y + DISTRACTOR_SIZE))
    return diss


def recreate_game(canvas, diss, sneaky):
    canvas.delete(sneaky)
    sneaky = create_sneaky(canvas)
    for i in diss:
        canvas.create_rectangle(*i)
    return sneaky


def hit(canvas, m, sneaky):
    overlapping_objects = canvas.find_overlapping(m.x, m.y, m.x, m.y)
    if len(overlapping_objects) == 1 and sneaky in overlapping_objects:
        return True
    return False


if __name__ == '__main__':
    main()
