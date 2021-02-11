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
        input("Ask a yes or no question: ")

        # remember, this is a comment
        # BEGIN YOUR CODE

        answers = ['Without a doubt.', 'Yes.', 'Ask again later.', 'No.', 'Karel thinks so.']

        num = random.randint(0,4)

        print(answers[num])

        # END YOUR CODE


        """num = random.randint(0, 4)

        if num == 0:
            answer = 'Without a doubt.'

        elif num == 1:
            answer = 'Yes.'

        elif num == 2:
            answer = 'Ask again later.'

        elif num == 3:
            answer = 'No'

        else:
            answer = 'Karel thinks so.'

        print(answer)"""

if __name__ == '__main__':
    main()