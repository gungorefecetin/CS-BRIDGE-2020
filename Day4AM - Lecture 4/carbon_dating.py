"""
File: carbon_dating.py
------------------
This program runs carbon dating (how cool!)
First, it prints out a lookup table that maps the percent
of c14 remaining to the number of years the sample has been
dead for, for the first 20 half lives.

Then, it prompts the user to enter a percent of c14, and it
will output the age of that sample.  It will re-prompt the user
until they enter -1, at which point the program will terminate.
"""


# This is needed to use the log function
import math


# The number of years it takes for the amount of c14 to be cut in half
C14_HALF_LIFE = 5700


def main():
    """
    You should replace this comment with a better, more descriptive one.
    You should delete the `pass` line below before writing your code.
    """
    # Milestone 1: Lookup Table

    print('Carbon Dating Lookup Table')
    print('Percent C-14 Remaining: years passed')

    years = 0
    percent = 100.0

    for i in range(20):
        print(str(percent) + '%' + ': ' + str(years))

        percent /= 2
        years += C14_HALF_LIFE

    print()

    # Milestone 2: Interactive Mode

    while True:
        percent = float(input('What percent of natural carbon-14 does your sample have? '))

        if percent == -1:
            break

        print('{} carbon-14...'.format(percent))

        age = (math.log(percent / 100) / math.log(1/2)) * C14_HALF_LIFE
        print('Your sample is ' + str(age) + ' years old.\n')


if __name__ == '__main__':
    main()