from turtle import Turtle
from random import choice

c = ['red', 'blue', 'green', 'yellow', 'purple', 'cyan', 'pink']
i = (10,9,8,7,-7,-8,-9,-10)

class Boll(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color(choice(c))
        self.x = choice(i)
        self.y = choice(i)
        self.s = 0.1

    def move(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)


    def bounce(self):
        self.y *= -1


    def rebounce(self):
        self.x *= -1

    def reposition(self):
        self.goto(0,0)
        self.rebounce()
