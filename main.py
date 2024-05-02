import sys
from pathlib import Path
import shutil
import turtle


def visit_folder(source: Path, dest: Path) -> None:
    if source.is_dir():
        for child in source.iterdir():
            visit_folder(child, dest)
    elif source.is_file():
        do_copy(source, dest)


def do_copy(file: Path, dest: Path):
    try:
        suffix = file.suffix[1:]
        if suffix == "":
            suffix = "no extension"
        file_dest = Path(dest.name + "/" + suffix)
        file_dest.mkdir(parents=True, exist_ok=True)
        shutil.copy(file, file_dest)
    except EnvironmentError:
        print(f"cannot copy {file.name}")


def main_1():
    args = sys.argv[1:]
    if len(args) == 0:
        print("Please add source path")
        return
    source_path = args[0]
    dest_path = "dest" if len(args) < 2 else args[1]
    source = Path(source_path)
    if not source.exists() and not source.is_dir():
        print("Please enter valid source path")
        return
    dest = Path(dest_path)
    if dest.exists() and not dest.is_dir():
        print("Please enter valid dest path")
        return
    if dest.exists():
        shutil.rmtree(dest)
    visit_folder(source, dest)


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_curve(t, order, size):
    koch_curve(t, order, size)


def draw_koch_snowflake(order: int, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    draw_koch_curve(t, order, size)
    t.right(120)
    draw_koch_curve(t, order, size)
    t.right(120)
    draw_koch_curve(t, order, size)

    window.mainloop()


def main_2():
    try:
        order = int(sys.argv[1])
        draw_koch_snowflake(order)
    except ValueError:
        print("Please enter correct order")


if __name__ == '__main__':
    # pass
    # main_1()
    main_2()
