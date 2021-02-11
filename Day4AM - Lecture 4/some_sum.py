"""
File: some_sum.py
-------------------
This program reads in 10 numbers from the user and prints
out the sum of those 10 numbers.
"""


def main():
    """
    You should replace this comment with a better, more descriptive one.
    You should delete the `pass` line below before writing your code.
    """

    # USING FOR LOOPS

    print('Enter 10 nums. I will show you the sum!')
    sum_of_ten_nums = 0

    for i in range(10):
        print('Please enter integer number ' + str(i+1) + ': ', end='')
        num = int(input())
        sum_of_ten_nums += num

    print('The sum is', sum_of_ten_nums)

    # USING WHILE LOOPS

    """print('Enter 10 nums. I will show you the sum!')
    sum_of_ten_nums1 = 0

    i = 0

    while i < 10:
        print('Please enter integer number ' + str(i + 1) + ': ', end='')
        num = int(input())

        sum_of_ten_nums1 += num
        
        i += 1

    print('The sum is', sum_of_ten_nums1)"""


if __name__ == '__main__':
    main()