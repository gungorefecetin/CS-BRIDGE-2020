from karel.stanfordkarel import *

"""
File: arches_karel.py
------------------------------
When you finish writing code in this file, arches_karel should
solve the "repair the quad" problem (or Charles Bridge, or Efes).
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """

    turn_left()
    build_column()

    while front_is_clear():
        move_to_another_spot()
        build_column()


def build_column():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

    for i in range(2):
        turn_left()

    while front_is_clear():
        move()

    turn_left()


def move_to_another_spot():
    for i in range(4):
        move()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point


if __name__ == "__main__":
    run_karel_program()
