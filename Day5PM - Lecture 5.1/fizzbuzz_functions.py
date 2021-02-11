"""
File: fizzbuzz_functions.py
--------------------
This program plays the game fizzbuzz up to a given number entered by the user.
"""


def main():
    # TODO: your code here (remove the 'pass' when you start)
    n = int(input('Number to count to: '))

    fizzbuzz(n)


def fizzbuzz(n):
    count_of_fizzed_or_buzzed = 0
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
            count_of_fizzed_or_buzzed += 1

        elif i % 3 == 0:
            print('Fizz')
            count_of_fizzed_or_buzzed += 1

        elif i % 5 == 0:
            print('Buzz')
            count_of_fizzed_or_buzzed += 1

        else:
            print(i)

    print(str(count_of_fizzed_or_buzzed) + ' numbers were fizzed or buzzed')


if __name__ == "__main__":
    main()
