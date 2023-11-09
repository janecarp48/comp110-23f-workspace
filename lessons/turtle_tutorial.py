"""Turtle practice bitches!"""

from turtle import Turtle, colormode, done
colormode(255)


leo: Turtle = Turtle()

def start_point(turtlename:str, x: int, y: int) -> None:
    turtlename.penup()
    turtlename.goto(x,y)
    turtlename.pendown()

start_point(leo, -110, -70)

def turtle_fill_color(turtlename: str, var1: int, var2: int, var3: int) -> None:
    """Enter 3 RGB variables to change the turtle color."""
    turtlename.fillcolor(var1, var2, var3)


def turtle_pen_color(turtlename: str, var1: int, var2: int, var3: int) -> None:
    """Enter 3 RGB variables to change the turtle color."""
    turtlename.pencolor(var1, var2, var3)

turtle_pen_color(leo, 100,0,0)
turtle_fill_color(leo, 10, 25, 200)

i: int = 0
leo.begin_fill()
while i < 3:
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

leo.hideturtle()

done() 

start_point(leo, -90, -50)
    turtle_fill_color(leo, 255, 255, 255)
    turtle_pen_color(leo, 0, 0, 0)
    rectangle_maker(leo, 50, 50)
    rectangle_maker(leo, 25, 25)
    start_point(leo,-65, -25)
    rectangle_maker(leo, 25, 25)
    """Window 2."""
    start_point(leo, 30, -50)
    rectangle_maker(leo, 50, 50)
    rectangle_maker(leo, 25, 25)
    start_point(leo, 55, -25)
    rectangle_maker(leo, 25, 25)
    """Window 3."""
    start_point(leo, 100, -50)
    rectangle_maker(leo, 50, 50)
    rectangle_maker(leo, 25, 25)
    start_point(leo, 125, -25)
    rectangle_maker(leo, 25, 25)