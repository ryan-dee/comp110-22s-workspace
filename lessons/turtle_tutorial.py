from turtle import Turtle, colormode, done
import turtle
leo: Turtle = Turtle()
leo.speed(50)
leo.hideturtle
colormode(255)
i: int = 0
leo.penup()
leo.goto(45, 60)
leo.pencolor(25, 74, 99)
leo.fillcolor(85, 218, 246)
leo.begin_fill()
while i < 3:
    leo.forward(300)
    leo.right(120)
    i = i + 1
leo.end_fill()


bob: Turtle = Turtle()
side_length: float = 300
colormode(255)
bob.speed(50)
bob.hideturtle
bob.penup()
bob.goto(45, 60)
bob.pendown()
bob.pencolor(85, 94, 246)
i: int = 0

while i < 3:
    bob.forward(side_length)
    bob.right(120)
    i = i + 1
    side_length

while i < 60:
    bob.forward(side_length)
    bob.right(122)
    i = i + 1
    side_length = side_length * .97
done()