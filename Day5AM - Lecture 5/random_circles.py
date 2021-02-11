"""
File: random_circles.py
-------------------
Draws 10 random circles such that each circle is on the screen.
"""

from graphics import Canvas
# this is needed to generate random numbers.  Don't delete this.
import random

# The number of circles to draw
NUM_CIRCLES = 10
MIN_RADIUS = 70
MAX_RADIUS = 200


def main():
    """
    You should write your code between the two lines written
    already that set up the canvas.
    You should replace this comment with a better, more descriptive one.
    """
    canvas = Canvas()
    canvas.set_canvas_title("Random Circles")

    height = canvas.get_canvas_height()
    width = canvas.get_canvas_width()


    for i in range(NUM_CIRCLES):
        radius = random.randint(MIN_RADIUS, MAX_RADIUS)

        x1 = random.randint(0, width - radius * 2)
        y1 = random.randint(0, height - radius * 2)

        circle = canvas.create_oval(x1, y1, x1 + 2 * radius, y1 + 2 * radius)
        color = canvas.get_random_color()

        canvas.set_fill_color(circle, color)

    # TODO: your code here

    canvas.mainloop()


# call the function
if __name__ == '__main__':
    main()
