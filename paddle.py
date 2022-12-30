import turtle


class Paddle(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.left(90)

    def set_right(self):
        self.setposition(350, 0)

    def set_left(self):
        self.setposition(-350, 0)

    def go_up(self):
        self.forward(20)
        pass

    def go_down(self):
        self.backward(20)
        pass
