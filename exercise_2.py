import sys
import turtle


def tree(t: turtle.Turtle, order: int, is_wide: bool, size: float):
    angle = 60 if is_wide else 30
    leaf_size = size if is_wide else size * 2 / 3
    t.forward(size)
    t.left(angle)
    t.forward(leaf_size)
    if order != 1:
        t.left(90 - angle)
        tree(t, order - 1, not is_wide, size if is_wide else size * 0.44)
        t.right(90)
        tree(t, order - 1, is_wide, size * 2 / 3)
        t.left(angle)
    t.backward(leaf_size)
    t.right(2 * angle)
    t.forward(leaf_size)
    if order != 1:
        t.right(90 - angle)
        tree(t, order - 1, not is_wide, size if is_wide else size * 0.44)
        t.left(90)
        tree(t, order - 1, is_wide, size * 2 / 3)
        t.right(angle)
    t.backward(leaf_size)
    t.left(angle)
    t.backward(size)


def draw_tree(order: int, size=160):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -size)
    t.left(90)
    t.pendown()

    tree(t, order, False, size)

    window.mainloop()


def main2():
    try:
        order = int(sys.argv[1])
        draw_tree(order)
    except ValueError:
        print("Please enter correct order")
