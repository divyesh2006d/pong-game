from turtle import *

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.goto(position)


    def move_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)


