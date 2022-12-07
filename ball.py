from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()

    def move(self):
        new_x = self.xcor() + 1
        new_y = self.ycor() + 1

        self.goto(new_x, new_y)

    def bounce(self):
        if self.ycor() > 300
        new_y =