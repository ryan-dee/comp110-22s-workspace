"""Childhood Home."""

__author__ = "730464883"

from random import randifrom turtle import Turtle, begin_fill, colormode, done


def main() -> None:
    """Final scene."""
    ertle: Turtle = Turtle()
    square(ertle, -350, 175)
    house(ertle, -175, 40)
    grass(ertle, -350, -80)
    roof(ertle, -175, 40)
    ws: int = 0
    while ws < 2:
        if ws == 0:
            windows(ertle, -155, 20)
        else:
            windows(ertle, -115, 20)
        ws = ws + 1
    x = randint(0, 120)
    y: int = randint(0, 10)
    tree(ertle, x, y)
    leaves(ertle, x, y)
    done()


def square(backgroun: Turtle, a: float, b: float) -> None:
    """Background of the scene."""
    colormode(255)
    background: Turtle = Turtle()
    background.pencolor(3, 4, 12)
    background.fillcolor(76, 83, 208)
    background.penup()
    background.goto(a, b)
    background.pendown()
    background.setheading(0.0)
    i: int = 0
    background.begin_fill()
    while i < 2:
        background.forward(700)
        background.right(90)
        background.forward(350)
        background.right(90)
        i = i + 1
    background.end_fill()


def house(color: Turtle, a: float, b: float) -> None:
    """Making the base of the Brown House."""
    colormode(255)
    house: Turtle = Turtle()
    house.pencolor(3, 4, 12)
    house.fillcolor(84, 48, 5)
    house.penup()
    house.goto(a, b)
    house.pendown()
    house.setheading(0.0)
    idx: int = 0
    house.begin_fill()
    while idx < 4:
        house.forward(120)
        house.right(90)
        idx = idx + 1
    house.end_fill()


def grass(color: Turtle, a: float, b: float) -> None: 
    """Making the grass from the yard for the house."""
    colormode(255)
    grass: Turtle = Turtle()
    grass.pencolor(3, 4, 12)
    grass.fillcolor(28, 176, 5)
    grass.penup()
    grass.goto(a, b)
    grass.pendown()
    grass.setheading(0.0)
    alt: int = 0
    grass.begin_fill()
    while alt < 2:
        grass.forward(700)
        grass.right(90)
        grass.forward(100)
        grass.right(90)
        alt = alt + 1
    grass.end_fill()


def roof(red: Turtle, a: float, b: float) -> None:
    """Roof of the red house."""
    colormode(255)
    roof: Turtle = Turtle()
    roof.pencolor(3, 4, 12)
    roof.fillcolor(188, 10, 46)
    roof.penup()
    roof.goto(a, b)
    roof.pendown()
    roof.setheading(0.0)
    v: int = 0
    roof.begin_fill()
    while v < 3:
        roof.forward(120)
        roof.left(120)
        v = v + 1
    roof.end_fill()


def windows(white: Turtle, a: float, b: float) -> None:
    """White windows that will be duplicate."""
    colormode(255)
    windows: Turtle = Turtle()
    windows.pencolor(3, 4, 12)
    windows.fillcolor(241, 246, 247)
    windows.penup()
    windows.goto(a, b)
    windows.pendown()
    windows.setheading(0.0)
    w: int = 0
    windows.begin_fill()
    while w < 4:
        windows.forward(30)
        windows.right(90)
        w = w + 1
    windows.end_fill()


def tree(tr: Turtle, a: int, b: int) -> None:
    """Tree that appears on a random place in the yard."""
    colormode(255)
    tree: Turtle = Turtle()
    tree.pencolor(3, 4, 12)
    tree.fillcolor(94, 43, 3)
    tree.penup()
    tree.goto(a, b)
    tree.pendown()
    tree.setheading(0.0)
    t: int = 0
    tree.begin_fill()
    length: int = randint(15, 70)
    width: int = randint(60, 150)
    while t < 2:
        tree.forward(length)
        tree.right(90)
        tree.forward(width)
        tree.right(90)
        t = t + 1
    tree.end_fill()


def leaves(le: Turtle, a: int, b: int) -> None:
    """Leaves that appear on top of the tree."""
    colormode(255)
    leaves: Turtle = Turtle()
    leaves.pencolor(3, 4, 12)
    leaves.fillcolor(28, 176, 5)
    leaves.penup()
    leaves.goto(a, b)
    leaves.pendown()
    leaves.setheading(0.0)
    leav: int = 0
    leaves.begin_fill()
    while leav < 4:
        leaves.forward(70)
        leaves.left(90)
        leav = leav + 1
    leaves.end_fill()


if __name__ == "__main__":
    main()
