from turtle import Turtle,Screen
from paddle import Paddle
from boll import Boll
from score import Score
import time

t = Turtle()
s = Screen()


s.setup(800,600)
s.bgcolor("black")
s.title("Pong")
s.tracer(0)

p_r = Paddle((350,0))
p_l = Paddle((-350,0))
b = Boll()
score = Score()
s.listen()

s.onkey(key='w',fun=p_l.move_up)
s.onkey(key='s',fun=p_l.move_down)

s.onkey(key='Up',fun=p_r.move_up)
s.onkey(key='Down',fun=p_r.move_down)

game = True
while game:
    time.sleep(b.s)
    s.update()
    b.move()

    if b.xcor() > 400 :
        b.reposition()
        score.upa()
        if not score.game:
            game = False

    if  b.xcor() < -400:
        b.reposition()
        score.upb()
        if not score.game:
            game = False

    # wall co
    if b.ycor() > 280 or b.ycor() < -280:
        b.bounce()

    #bounce with paddle
    if b.distance(p_r) < 50 and b.xcor() > 340 or b.distance(p_l) < 50 and b.xcor() < -340 :
        b.rebounce()


s.exitonclick()