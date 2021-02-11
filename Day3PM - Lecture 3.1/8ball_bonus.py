"""
File: 8ball.py
-------------------
Simulates an eight ball and gives sage answers to
yes or no questions.
"""

# This is needed to generate random numbers
import random


def main():
    while True:
        question = input("Ask a yes or no question: ")

        # remember, this is a comment
        # BEGIN YOUR CODE

        if question == '':
            print('nothing entered')
            break

        answers = ['Without a doubt.', 'Yes.', 'Ask again later.', 'No.', 'Karel thinks so.']

        num = random.randint(0, 4)

        print(answers[num])

        # END YOUR CODE


if __name__ == '__main__':
    main()
