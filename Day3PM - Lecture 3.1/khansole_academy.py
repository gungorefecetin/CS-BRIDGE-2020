"""
File: khansole_academy.py
-------------------
This program generates random addition problems for the user to solve, and gives
them feedback on whether their answer is right or wrong.  It keeps giving them
practice problems until they answer correctly 3 times in a row.
"""


# This is needed to generate random numbers
import random


def main():
    # Your code here
    # Delete the `pass` line before starting to write your own code

    counter = 0

    while True:
        num1, num2 = random.randint(10, 99), random.randint(10, 99)
        answer = int(input('What is ' + str(num1) + ' + ' + str(num2) + '? '))
        if answer == num1 + num2:
            counter += 1
            print("Correct! You've gotten " + str(counter) + " correct in a row.")
        else:
            print('Incorrect. The expected answer is ' + str(num1 + num2))
            counter = 0
        if counter == 3:
            print('Congratulations! You mastered addition.')
            break


if __name__ == "__main__":
    main()
