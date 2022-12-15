from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

#creating objects
ball = Ball()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
scoreboard = Scoreboard()


screen.listen()

screen.onkey(l_paddle.move_up, "Up")
screen.onkey(l_paddle.move_down, "Down")
screen.onkey(r_paddle.move_up, "w")
screen.onkey(r_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # BOUNCE
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() > -340:
       ball.bounce_x()

    # Detect right paddle miss
    if ball.xcor() > 380:
       ball.reset_position()
       scoreboard.l_point()
       scoreboard.update_scoreboard()
       ball.bounce_y()

    # Detect left paddle miss
    if ball.xcor() < -380:
       ball.reset_position()
       scoreboard.r_point()
       scoreboard.update_scoreboard()
       ball.bounce_x()

screen.exitonclick()
