"""
File: running_sum.py
-------------------
This program reads in integers from the user
and then keeps outputting the sum of the entered values.
"""


def main():
    # Your code here
    # Delete the `pass` line before starting to write your own code

    # print('Enter integers, one at a time. I will show you the sum! (Press "q" for exit.)')
    # running_sum_v1()
    running_sum()


def running_sum():
    sum_of_numbers = 0
    counter = 0
    while True:
        n = int(input('Please enter an integer: '))

        counter += 1

        n = int(n)
        sum_of_numbers += n
        print('The current sum is: {} ({} integers entered)'.format(sum_of_numbers, counter))


if __name__ == '__main__':
    main()
