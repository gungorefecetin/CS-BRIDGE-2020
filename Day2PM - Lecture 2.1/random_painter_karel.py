from karel.stanfordkarel import *

"""
File: random_painter_karel.py
------------------------------
Your job is to paint random squares all over the world!
Pick two colors and choose randomly between them for each
square.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """

    paint()

    while left_is_clear():
        return_back_and_move_to_next_row()
        paint()


def paint():
    Colors = [MAGENTA, GREEN]
    paint_corner(Colors[random(0.5)])
    while front_is_clear():
        move()
        paint_corner(Colors[random(0.5)])


def return_back_and_move_to_next_row():
    turn_left()
    turn_left()

    while front_is_clear():
        move()
    turn_right()

    move()
    turn_right()


def turn_right():
    for i in range(3):
        turn_left()
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
