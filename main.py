from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color('black')


def draw_square():
    timmy.forward(200)
    timmy.left(90)
    timmy.forward(200)
    timmy.left(90)
    timmy.forward(200)
    timmy.left(90)
    timmy.forward(200)
    timmy.left(90)


draw_square()

screen = Screen()
screen.exitonclick()
