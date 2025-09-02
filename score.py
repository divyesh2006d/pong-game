from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreA = 0
        self.scoreB = 0
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.update()
        self.hideturtle()
        self.game = True


    def update(self):
        self.write(f'{self.scoreA}   {self.scoreB}', align='center', font=('Courier', 30, 'normal'))

    def game_over(self,team):
        self.goto(0, 0)
        self.color('red')
        self.write(f'Game Over : {team}', align='center', font=('Courier', 24, 'normal'))

    def upa(self):
        self.clear()
        self.scoreA += 1
        self.update()
        g = 'A win'
        if self.scoreA == 5:
            self.game_over(g)
            self.game = False

    def upb(self):
        self.clear()
        self.scoreB += 1
        self.update()
        k = 'B win'
        if self.scoreB == 5:
            self.game_over(k)
            self.game = False

