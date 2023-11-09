"""TODO: Bob Ross style sketch of a cabin and some trees."""


from turtle import Turtle, colormode, done
colormode(255)


__author__ = 730555961


def main() -> None:
    """Code to actually create my scene."""
    leo: Turtle = Turtle()
    """Mountains."""
    start_point(leo, -300, -70)
    turtle_fill_color(leo, 0, 0, 128)
    triangle_maker(leo, 400)
    start_point(leo, -175, -70)
    triangle_maker(leo, 400)
    start_point(leo, -50, -70)
    triangle_maker(leo, 400)
    """Grass."""
    start_point(leo, -300, -250)
    turtle_fill_color(leo, 0, 100, 10)
    rectangle_maker(leo, 185, 750)
    """House Construction."""
    start_point(leo, -120, -70)
    turtle_pen_color(leo, 0, 0, 0)
    turtle_fill_color(leo, 100, 0, 0)
    rectangle_maker(leo, 120, 300)
    """Door."""
    start_point(leo, -20, -70)
    turtle_pen_color(leo, 255, 255, 255)
    turtle_fill_color(leo, 0, 0, 0)
    rectangle_maker(leo, 60, 30)
    """Doorknob. I am attempting to create a cute little golden knob for my door."""
    start_point(leo, 5, -50)
    turtle_pen_color(leo, 255, 215, 0)
    turtle_fill_color(leo, 255, 215, 0)
    leo.begin_fill()
    leo.circle(2.5)
    leo.end_fill()
    """Windows."""
    """Window 1."""
    window_maker(leo, -90, -50, 50, 25)
    """Window 2."""
    window_maker(leo, 30, -50, 50, 25)
    """Window 3."""
    window_maker(leo, 100, -50, 50, 25)
    """Trees."""
    """Tree 1."""
    start_point(leo, -190, -40)
    turtle_fill_color(leo, 0, 100, 10)
    triangle_maker(leo, 80)
    start_point(leo, -190, -20)
    triangle_maker(leo, 80)
    turtle_fill_color(leo, 150, 75, 0)
    start_point(leo, -155, -70)
    rectangle_maker(leo, 30, 10)
    """Tree 2."""
    start_point(leo, 140, -40)
    turtle_fill_color(leo, 0, 100, 10)
    triangle_maker(leo, 80)
    start_point(leo, 140, -20)
    triangle_maker(leo, 80)
    turtle_fill_color(leo, 150, 75, 0)
    start_point(leo, 175, -70)
    rectangle_maker(leo, 30, 10)
    leo.hideturtle()


def window_maker(turtlename: Turtle, x: float, y: float, windowwidth: float, panelwidth: float) -> None:
    """Creates a square window given a starting point, window width, and panel width."""
    start_point(turtlename, x, y)
    turtle_fill_color(turtlename, 255, 255, 255)
    turtle_pen_color(turtlename, 0, 0, 0)
    rectangle_maker(turtlename, windowwidth, windowwidth)
    rectangle_maker(turtlename, panelwidth, panelwidth)
    start_point(turtlename, (x + panelwidth), (y + panelwidth))
    rectangle_maker(turtlename, panelwidth, panelwidth)
    

def start_point(turtlename: Turtle, x: float, y: float) -> None:
    """Starting coordinates of turtle."""
    turtlename.penup()
    turtlename.goto(x, y)
    turtlename.pendown()


def rectangle_maker(turtlename: Turtle, len: float, width: float) -> None:
    """Creates a rectangle given a length and width."""
    turtlename.begin_fill()
    i: int = 0
    while i < 2:
        turtlename.forward(width)
        turtlename.left(90)
        turtlename.forward(len)
        turtlename.left(90)
        i = i + 1
    turtlename.end_fill()


def triangle_maker(turtlename: Turtle, len: int) -> None:
    """Creates an equilateral triangle given a length."""
    i: int = 0
    turtlename.begin_fill()
    while i < 3:
        turtlename.forward(len)
        turtlename.left(120)
        i = i + 1
    turtlename.end_fill()


def turtle_fill_color(turtlename: Turtle, var1: float, var2: float, var3: float) -> None:
    """Enter 3 RGB variables to change the turtle color."""
    turtlename.fillcolor(var1, var2, var3)


def turtle_pen_color(turtlename: Turtle, var1: float, var2: float, var3: float) -> None:
    """Enter 3 RGB variables to change the turtle color."""
    turtlename.pencolor(var1, var2, var3)


if __name__ == "__main__":
    main()
    done()