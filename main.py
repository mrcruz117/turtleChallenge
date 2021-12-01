from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color('black')


def dash_line(length):
    for amount in range(length):
        timmy.forward(5)
        timmy.penup()
        timmy.forward(5)
        timmy.pendown()


def draw_square():
    dash_line(20)
    timmy.left(90)
    dash_line(20)
    timmy.left(90)
    dash_line(20)
    timmy.left(90)
    dash_line(20)
    timmy.left(90)


draw_square()

screen = Screen()
screen.exitonclick()
