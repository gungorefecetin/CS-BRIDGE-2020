"""
File: moon.py
------------------
Converts weight on earth into weight on the moon.
"""


def main():
    # Your code here
    # Delete the `pass` line before starting to write your own code

    e_weight = float(input('Enter a weight on earth: '))

    m_weight = calculate_the_moon_weight(e_weight)
    print('Your height on the moon is:', m_weight)


def calculate_the_moon_weight(e_weight):
    return e_weight * 16.5 / 100


if __name__ == "__main__":
    main()