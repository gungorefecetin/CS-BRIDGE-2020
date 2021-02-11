from karel.stanfordkarel import *

"""
File: collect_newspaper_karel.py
------------------------------
At present, the collect_newspaper_karel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """

    move_to_newspaper()
    pick_up_newspaper()
    move_to_start()

def turn_right():
    for i in range(3):
        turn_left()

def move_to_newspaper():
    for i in range(2):
        move()
    turn_right()
    move()
    turn_left()
    move()

def pick_up_newspaper():
    pick_beeper()

def move_to_start():
    for i in range(2):
        turn_left()
    move()
    turn_right()
    move()
    turn_left()
    for i in range(2):
        move()

    for i in range(2):
        turn_right()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
