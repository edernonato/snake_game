from turtle import Turtle
from random import choice

cor = []
for n in range(-280, 280):
    if n % 20 == 0:
        cor.append(float(n))


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("purple")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.change_position()

    def change_position(self):
        x = choice(cor)
        y = choice(cor)
        self.goto(x, y)




