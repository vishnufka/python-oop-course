import numpy as np
from PIL import Image, ImageDraw


class Canvas:

    def __init__(self, w, h, color):
        self.w = w
        self.h = h
        self.color = color

    def make(self):
        return Image.new("RGB", (int(self.w), int(self.h)), "white" if self.color == "w" else "black")


class Rectangle:

    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

    def draw(self, canvas):
        ImageDraw.Draw(canvas).rectangle((self.x, self.y, self.w, self.h), fill=self.color)


class Square:

    def __init__(self, x, y, w, color):
        self.x = x
        self.y = y
        self.w = w
        self.color = color

    def draw(self, canvas):
        ImageDraw.Draw(canvas).rectangle((self.x, self.y, self.w, self.w), fill=self.color)


def main():
    print("Welcome to the canvas drawing app!\n")
    w = int(input("enter canvas width: "))
    h = int(input("enter canvas height: "))
    color = input("enter canvas color b/w: ")
    canvas = Canvas.make(Canvas(w, h, color))

    while True:
        shape = input("what shape do you want to draw s/r? type q to quit: ")
        if shape == "q":
            break
        if shape != "s" and shape != "r":
            continue

        x = int(input("enter x coord: "))
        y = int(input("enter y coord: "))
        w = int(input("enter width: "))
        if shape == "r":
            h = int(input("enter height: "))
        r = int(input("enter color r: "))
        g = int(input("enter color g: "))
        b = int(input("enter color b: "))

        if shape == "s":
            square = Square(x, y, w, (r, g, b))
            square.draw(canvas)
            print("drew a square!")
        elif shape == "r":
            rectangle = Rectangle(x, y, w, h, (r, g, b))
            rectangle.draw(canvas)
            print("drew a rectangle!")

    canvas.save("canvas.png")


if __name__ == "__main__":
    main()
