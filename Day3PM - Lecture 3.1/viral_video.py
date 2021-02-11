"""
File: viral_video.py
-------------------
This program asks the user for a target number of video views
and a growth rate, and calculates how many view the video creator
will get over time and how many days it will take to get to the target
number of views.
"""


def main():
    # Your code here
    # Delete the `pass` line before starting to write your own code

    num_of_views = float(input('Please enter the target of views: '))
    growth_rate = float(input('Please enter the growth rate: '))

    growth_rate_value = growth_rate

    print('Day 1: 1 view')

    day_counter = 2

    while growth_rate <= num_of_views:
        print('Day ' + str(day_counter) + ': ' + str(growth_rate) + ' view')
        growth_rate *= growth_rate_value

        day_counter += 1

    print('Day ' + str(day_counter) + ': ' + str(growth_rate))

    print('It took you ' + str(day_counter) + ' days to reach or exceed your goal of ' + str(num_of_views) + ' views!')


if __name__ == "__main__":
    main()
