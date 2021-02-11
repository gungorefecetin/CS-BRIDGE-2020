"""
File: is_ascending.py
-------------------
This program prompts the user for numbers until they enter -1, and then
prints out the numbers and whether or not those numbers are in ascending order.
"""


def main():
    # TODO: your code here! (remove the pass when you start)

    numbers = list()

    while True:
        num = int(input('> '))

        if num == -1:
            break

        else:
            numbers.append(num)

    for num in numbers:
        print(num)

    if is_ascending(numbers):
        print('Ascending!')

    else:
        print('Not ascending')


def is_ascending(numbers):
    return sorted(numbers) == numbers


if __name__ == '__main__':
    main()
