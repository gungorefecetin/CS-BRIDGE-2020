"""
File: programming_is_awesome.py
--------------------
This program draws various art on the canvas using graphics!
"""

from graphics import Canvas


def main():
    """
    You should write your code between the two lines written
    already that set up the canvas.
    You should replace this comment with a better, more descriptive one.
    """
    canvas = Canvas()
    canvas.set_canvas_title("Programming is Awesome!")

    # TODO: your code here

    r1 = canvas.create_rectangle(100, 200, 300, 400)
    r2 = canvas.create_rectangle(400, 400, 500, 300)
    r3 = canvas.create_rectangle(600, 100, 700, 400)

    canvas.set_color(r1, 'red')
    canvas.set_color(r2, 'blue')
    canvas.set_color(r3, 'yellow')

    text = canvas.create_text(canvas.get_canvas_width() / 2, canvas.get_canvas_height() / 2, 'Programming is awesome!')
    canvas.set_font(text, 'Courier', 30)

    canvas.mainloop()


if __name__ == '__main__':
    main()
