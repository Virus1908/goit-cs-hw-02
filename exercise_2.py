import sys
import turtle
import math


def tree(t: turtle.Turtle, order: int, size: float):
    t.forward(size)
    t.left(45)
    t.forward(size * math.sqrt(2) / 2)
    if order != 1:
        t.left(45)
        tree(t, order - 1, size / 2)
        t.right(45)
    t.backward(size * math.sqrt(2) / 2)
    t.right(90)
    t.forward(size * math.sqrt(2) / 2)
    if order != 1:
        t.right(45)
        tree(t, order - 1, size / 2)
        t.left(45)
    t.backward(size * math.sqrt(2) / 2)
    t.left(45)
    t.backward(size)


def draw_tree(order: int, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -size)
    t.left(90)
    t.pendown()

    tree(t, order, size)

    window.mainloop()


def main2():
    try:
        order = int(sys.argv[1])
        draw_tree(order)
    except ValueError:
        print("Please enter correct order")
