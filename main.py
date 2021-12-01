from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color('black')

screen = Screen()
screen.colormode(255)


def draw_polygon(sides):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy.pencolor(r, g, b)
    angle = 360 / sides

    for num in range(sides):
        timmy.forward(100)
        timmy.left(angle)


draw_polygon(3)
draw_polygon(4)
draw_polygon(5)
draw_polygon(6)
draw_polygon(7)
draw_polygon(8)

screen.exitonclick()
