"""
File: print_indices.py
-------------------
This program prints out the indices of a 5x5 grid, row by row.
"""

NUM_ROW = 5
NUM_COL = 5


def main():
    # TODO: your code here (remove the 'pass' when you start)
    for i in range(NUM_ROW):
        for j in range(NUM_COL):
            if j == NUM_COL - 1:  # If it is last line, don't use comma on
                print('(' + str(j) + ',' + str(i) + ')', end = '')
                break

            print('(' + str(j) + ',' + str(i) + '),', end = '')

        print()

    """for i in range(NUM_OF_ITERATIONS):
        for j in range(NUM_OF_ITERATIONS):
            print('({},{})'.format(j, i))"""


if __name__ == '__main__':
    main()
