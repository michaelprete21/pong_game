import turtle
from paddle import Paddle
from ball import Ball
import time
import random

t = turtle.Turtle()
sc = turtle.Screen()
sc.setup(800, 600)
sc.bgcolor("black")
sc.title("Pong")
sc.listen()
sc.tracer(0)
right_points = 0
left_points = 0



#Create the paddles and set their positions
right_paddle = Paddle()
right_paddle.set_right()
left_paddle = Paddle()
left_paddle.set_left()

sc.onkey(right_paddle.go_up, "Up")
sc.onkey(right_paddle.go_down, "Down")
sc.onkey(left_paddle.go_up, "w")
sc.onkey(left_paddle.go_down, "s")

#create the ball
direction = random.randint(0,180)
ball = Ball(direction)

game_is_on = True

while game_is_on:
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    ball.move_ball()
    time.sleep(.0001)
    sc.update()
    #Detect collision with r_paddle.
    if ball.distance(right_paddle) <50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    elif ball.xcor() > 370:
        right_points += 1
        print(right_points)
        ball.reset_position()
    elif ball.xcor() < -370:
        left_points += 1
        print(left_points)
        ball.reset_position()

game_is_on = True




sc.exitonclick()
