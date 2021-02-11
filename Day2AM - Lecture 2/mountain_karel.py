from karel.stanfordkarel import *

"""
File: mountain_karel.py
------------------------------
At present, this file does nothing. Your job is to place
a beeper at the top of the mountain. You should make sure
that your program works for all of the sample mountain worlds
supplied in the starter folder.
"""


def turn_right():
    for i in range(3):
        turn_left()


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """

    climb_the_mountain()
    put_beeper()
    descend_from_the_mountain()


def climb_the_mountain():
    while front_is_blocked():
        turn_left()
        move()
        turn_right()
        move()

def descend_from_the_mountain():
    while front_is_clear():
        move()
        turn_right()
        move()
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
