from turtle import Turtle,Screen
import time
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")
screen.tracer(0)
ball = Ball()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)


screen.listen()

screen.onkey(l_paddle.move_up,"Up")
screen.onkey(l_paddle.move_down, "Down")
screen.onkey(r_paddle.move_up,"w")
screen.onkey(r_paddle.move_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 300 or ball.ycor() < -300:
        #BOUNCE




screen.exitonclick()


