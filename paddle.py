from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, xcord, ycord):
        super().__init__()
        self.xcord = xcord
        self.ycord = ycord
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(self.xcord, self.ycord)
        self.color("white")
        self.penup()


    def move_up(self):
        new_y = (self.ycor() + 20)
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = (self.ycor() - 20)
        self.goto(self.xcor(), new_y)