from karel.stanfordkarel import *

"""
File: stripe_karel.py
------------------------------
At present, this file does nothing. Your job is to place
a line of beepers on every odd row. You can assume that there
are an odd number of rows in the world, and you should make sure
that your program works for all of the sample stripe worlds.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """

    draw_stripe()
    come_back()

    while left_is_clear():
        move_to_another_spot()

        if left_is_clear():
            move_to_another_spot()
            draw_stripe()
            come_back()



def draw_stripe():
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()


def come_back():
    for i in range(2):
        turn_left()

    while front_is_clear():
        move()

    for i in range(2):
        turn_left()


def move_to_another_spot():
    turn_left()
    move()
    turn_right()



def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
