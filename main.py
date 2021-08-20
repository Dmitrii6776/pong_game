from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.dawn, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.dawn, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()
    elif ball.distance(r_paddle) < 60 and ball.xcor() > 330 or ball.distance(l_paddle) < 60 and ball.xcor() < -330:
        ball.paddle_bounce()
    elif ball.xcor() > 390:
        ball.reset()
        scoreboard.l_point()

    elif ball.xcor() < -390:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
