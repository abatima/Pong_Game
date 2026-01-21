from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, xcor):
        super().__init__()
        self.xcor = xcor
        self.create_paddle(self.xcor)

    def create_paddle(self, xcor):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.teleport(self.xcor, 0)

    def go_up(self):
        new_ycor = self.ycor() + 20
        self.teleport(self.xcor, new_ycor)

    def go_down(self):
        new_ycor = self.ycor() - 20
        self.teleport(self.xcor, new_ycor)
