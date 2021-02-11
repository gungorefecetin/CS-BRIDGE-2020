from karel.stanfordkarel import *

"""
File: hospital_karel.py
------------------------------
Your job is to help Karel build new hospitals in
the places marked by each beeper in the original world.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    move_to_another_beeper()
    build_hospital()

    while front_is_clear():
        move_to_another_beeper()
        build_hospital()


def move_to_another_beeper():
    while no_beepers_present():
        move()
    move()


def build_hospital():
    put_beeper()
    turn_left()

    move()

    put_beeper()
    turn_left()

    move()

    put_beeper()
    turn_right()

    move()

    put_beeper()
    turn_right()

    move()

    put_beeper()
    turn_right()

    for i in range(2):
        move()
    turn_left()

    if front_is_clear():
        move()


def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
