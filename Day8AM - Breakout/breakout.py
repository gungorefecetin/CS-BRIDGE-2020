"""
File: breakout.py
-----------------
This program implements the game Breakout!  The user controls a paddle
moving horizontally with the mouse, and the user must bounce the ball
to make it collide and remove bricks from the screen.  The user has
3 turns.  If the ball falls below the bottom of the screen, the user
loses a turn.  If the user removes all bricks before their turns
run out, they win!
"""

import math
from graphics import Canvas
import random
import time

"""
Dimensions of the canvas, in pixels
These should be used when setting up the initial size of the game,
but in later calculations you should use canvas.get_canvas_width() and 
canvas.get_canvas_height() rather than these constants for accurate size information.
"""
CANVAS_WIDTH = 420
CANVAS_HEIGHT = 600

# Stage 1: Set up the Bricks

# Number of bricks in each row
NBRICK_COLUMNS = 10

# Number of rows of bricks
NBRICK_ROWS = 10

# Separation between neighboring bricks, in pixels
BRICK_SEP = 4

# Width of each brick, in pixels
BRICK_WIDTH = math.floor((CANVAS_WIDTH - (NBRICK_COLUMNS + 1.0) * BRICK_SEP) / NBRICK_COLUMNS)

# Height of each brick, in pixels
BRICK_HEIGHT = 8

# Offset of the top brick row from the top, in pixels
BRICK_Y_OFFSET = 70

# Stage 2: Create the Bouncing Ball

# Radius of the ball in pixels
BALL_RADIUS = 10
BALL_SIZE = BALL_RADIUS * 2

# The ball's vertical velocity.
VELOCITY_Y = 6.0

# The ball's minimum and maximum horizontal velocity; the bounds of the
# initial random velocity that you should choose (randomly +/-).
VELOCITY_X_MIN = 2.0
VELOCITY_X_MAX = 6.0

# Animation delay or pause time between ball moves (in seconds)
DELAY = 1 / 60

# Stage 3: Create the Paddle

# Dimensions of the paddle
PADDLE_WIDTH = 60
PADDLE_HEIGHT = 10

# Offset of the paddle up from the bottom
PADDLE_Y_OFFSET = 30

# Stage 5: Polish and Finishing Up

# Number of turns
NTURNS = 3

BOUNCE_SOUND = "bounce.au"


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("Breakout")

    # Game Start

    bricks = create_bricks(canvas)
    paddle = create_paddle(canvas)
    ball = create_ball(canvas)

    nturns = NTURNS

    velocity_y = VELOCITY_Y
    velocity_x = random.randint(VELOCITY_X_MIN, VELOCITY_X_MAX)

    score = 0

    canvas.wait_for_click()

    while True:
        if canvas.mouse_is_on_canvas():  # If mouse is out of canvas, it stops
            mouse_x = canvas.get_mouse_x()

            mouse_x = max(PADDLE_WIDTH // 2, mouse_x)
            mouse_x = min(mouse_x, CANVAS_WIDTH - PADDLE_WIDTH // 2)

            canvas.moveto(paddle, mouse_x - PADDLE_WIDTH // 2, CANVAS_HEIGHT - PADDLE_Y_OFFSET)

        canvas.move(ball, velocity_x, velocity_y)

        if canvas.get_top_y(ball) + BALL_SIZE >= CANVAS_HEIGHT:
            nturns -= 1

            if nturns == 0:
                canvas.delete(ball)
                game_over(canvas, score)
                break

            restart(canvas, ball)
            canvas.wait_for_click()

        elif canvas.get_top_y(ball) <= 0:
            velocity_y = -velocity_y

        if canvas.get_left_x(ball) <= 0:
            velocity_x = -velocity_x

        elif canvas.get_left_x(ball) + BALL_SIZE >= CANVAS_WIDTH:
            velocity_x = -velocity_x

        # BREAKING THE BRICKS

        ball_coords = canvas.coords(ball)

        x1, y1, x2, y2 = ball_coords[0], ball_coords[1], ball_coords[2], ball_coords[3]
        colliding_list = canvas.find_overlapping(x1, y1, x2, y2)

        for object in colliding_list:
            if object != ball:  # ball is in the colliding list, we ignore it
                if object == paddle:  # if ball hits paddle, change the direction_y
                    velocity_y = -abs(velocity_y)

                else:  # if ball hits the brick
                    if break_bricks_control_1(canvas, object):
                        velocity_y = -velocity_y

                    if break_bricks_control_2(canvas, object):
                        velocity_x = -velocity_x

                    canvas.delete(object)  # delete that brick from canvas

                    if object in bricks:
                        bricks.remove(object)  # delete that brick from bricks list
                        score += 1
                        break

        if len(bricks) == 0:
            winning_message(canvas)
            canvas.delete(ball)
            break

        canvas.update()
        time.sleep(DELAY)

    # print(score)

    canvas.mainloop()


def create_bricks(canvas):
    bricks = []
    for x in range(NBRICK_ROWS):
        for y in range(NBRICK_COLUMNS):
            brick = canvas.create_rectangle(y * BRICK_WIDTH + (y + 1) * BRICK_SEP,
                                            BRICK_Y_OFFSET + x * BRICK_HEIGHT + x * BRICK_SEP,
                                            (y + 1) * BRICK_WIDTH + (y + 1) * BRICK_SEP,
                                            BRICK_Y_OFFSET + (x + 1) * BRICK_HEIGHT + x * BRICK_SEP, )

            canvas.set_fill_color(brick, set_brick_color(x))
            bricks.append(brick)

    return bricks


def set_brick_color(x):
    if x < 2:
        return 'red'

    elif x < 4:
        return 'orange'

    elif x < 6:
        return 'green'

    elif x < 8:
        return 'cyan'

    else:
        return 'blue'


def restart(canvas, ball):
    canvas.moveto(ball, CANVAS_WIDTH // 2 - BALL_RADIUS, CANVAS_HEIGHT // 2 - BALL_RADIUS)


def create_paddle(canvas):
    paddle = canvas.create_rectangle(CANVAS_WIDTH // 2 - PADDLE_WIDTH // 2,
                                     CANVAS_HEIGHT - PADDLE_Y_OFFSET - PADDLE_HEIGHT,
                                     CANVAS_WIDTH // 2 + PADDLE_WIDTH // 2,
                                     CANVAS_HEIGHT - PADDLE_Y_OFFSET)

    canvas.set_fill_color(paddle, 'black')

    return paddle


def create_ball(canvas):
    ball = canvas.create_oval(CANVAS_WIDTH // 2 - BALL_RADIUS, CANVAS_HEIGHT // 2 - BALL_RADIUS,
                              CANVAS_WIDTH // 2 + BALL_RADIUS, CANVAS_HEIGHT // 2 + BALL_RADIUS)

    canvas.set_fill_color(ball, 'black')
    return ball


def break_bricks_control_1(canvas, object):
    return canvas.get_left_x(object) < canvas.get_left_x(object) + BALL_RADIUS < canvas.get_left_x(object) + BRICK_WIDTH


def break_bricks_control_2(canvas, object):
    return canvas.get_top_y(object) < canvas.get_top_y(object) + BALL_RADIUS < canvas.get_top_y(object) + BRICK_HEIGHT


def game_over(canvas, score):
    text = canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, 'GAME OVER!')
    text1 = canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2 + 100, 'Score: ' + str(score))
    canvas.set_font(text, 'Courier', 50)
    canvas.set_font(text1, 'Courier', 50)


def winning_message(canvas):
    text = canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, 'YOU WON!')
    text1 = canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2 + 100, 'Score: 100')
    canvas.set_font(text, 'Courier', 50)
    canvas.set_font(text1, 'Courier', 50)


if __name__ == '__main__':
    main()
