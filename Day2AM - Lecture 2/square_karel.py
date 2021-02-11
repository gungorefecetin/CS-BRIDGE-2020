from karel.stanfordkarel import *

"""
File: square_karel.py
------------------------------
Your job is to write a program that lets Karel place an outline
of beepers in a square world. You should make sure that
your program works for all of the sample square worlds,
like 8x8, 5x5, 3x3, 2x2, and 1x1.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    draw_square()
    # bonus_part()


def draw_square():
    for i in range(4):
        while front_is_clear():
            move()
            put_beeper()

        while front_is_blocked():
            turn_left()
            break


def bonus_part():
    turn_left()
    if front_is_clear():
        move()
        turn_right()
        move()

    for i in range(4):
        while front_is_clear():
            if front_is_clear():
                move()
                put_beeper()

            if front_is_blocked():
                pick_beeper()
                for j in range(2):
                    turn_left()
                move()

                turn_right()
                break


def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
