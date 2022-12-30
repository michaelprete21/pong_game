import turtle
import random


class Ball(turtle.Turtle):

    def __init__(self, direction):
        super().__init__()
        self.speed("slow")
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setheading(direction)
        self.x_move = 1
        self.y_move = 1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= - 1

    def reset_position(self):
        self.setposition(0,0)
        self.bounce_x()
