"""
File: bouncing_ball.py
---------------------
This program animates a ball (circle) bouncing around the screen.
"""

from graphics import Canvas

# Needed to place the ball randomly on the canvas.  Don't remove this.

# Needed to delay the animation.  Don't remove this.
import time

# Size of the ball
BALL_RADIUS = 20
BALL_SIZE = BALL_RADIUS * 2

BALL_SPEED = 9

# Seconds to pause each animation cycle
DELAY = 0.03

"""
The value of the speed in the x and y direction the ball should travel.
In other words, the ball will be traveling either +5 or -5 in the x direction, and
+5 or -5 in the y direction, at all times.
"""

CANVAS_WIDTH = 754
CANVAS_HEIGHT = 492


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Bouncing Ball")

    width = canvas.get_canvas_width()
    height = canvas.get_canvas_height()

    change_x = 5
    change_y = 5

    ball = canvas.create_oval(0, 0, BALL_SIZE, BALL_SIZE)
    canvas.set_color(ball, 'blue')

    while True:

        if canvas.get_left_x(ball) == 0 and canvas.get_top_y(ball) == 0:
            change_x = -change_x
            change_y = -change_y

        if canvas.get_top_y(ball) + BALL_SIZE >= height:
            change_y = -change_y  # alt duvar

        elif canvas.get_top_y(ball) <= 0:
            change_y = -change_y # sağ duvar

        if canvas.get_left_x(ball) <= 0:
            change_x = -change_x # üst

        elif canvas.get_left_x(ball) + BALL_SIZE >= width:
            change_x = -change_x

        canvas.move(ball, change_x, change_y)

        canvas.update()
        time.sleep(DELAY)

    canvas.mainloop()


if __name__ == "__main__":
    main()
