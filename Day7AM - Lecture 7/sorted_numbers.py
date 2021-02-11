"""
File: sorted_numbers.py
-------------------
This program prompts the user for 10 numbers, and then
prints out those numbers in sorted order.
"""

LEN_OF_NUMBERS = 10


def main():
    # TODO: your code here! (remove the pass when you start)

    numbers = list()

    for i in range(LEN_OF_NUMBERS):
        numbers.append(int(input()))

    # numbers = sorted(numbers)
    numbers.sort()

    for i in numbers:
        print(i)


if __name__ == '__main__':
    main()
