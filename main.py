import turtle
from time import sleep
try:
    turtle.bgcolor("blue")
    turtle.pensize(2)
    turtle.speed(0)
    for i in range(0, 6):
        for colors in ["red", "magenta", "blue", "cyan", "black", "yellow", "white"]:
                turtle.color(colors)
                turtle.circle(100)
                turtle.right(10)
    sleep(5)
    turtle.hideturtle()
except KeyboardInterrupt:
    print("exiting spiral program")
    exit()