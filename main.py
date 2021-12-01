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


def random_walk(num_of_turns):
    timmy.speed(0)
    for num in range(num_of_turns):
        choices = ['left', 'right']
        choice = random.choice(choices)
        angle = random.randint(0, 360)
        distance = random.randint(0, 100)
        timmy.forward(distance)
        if choice == 'left':
            timmy.left(angle)
        if choice == 'right':
            timmy.right(angle)


def spirograph():
    timmy.speed(0)
    for num in range(180):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        timmy.pencolor(r, g, b)
        timmy.circle(100)
        timmy.left(2)


spirograph()
# random_walk(100)
screen.exitonclick()
