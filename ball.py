from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        self.shape("circle")
        self.color("white")

    def move(self):
        new_xcor = self.xcor() + 1
        new_ycor = self.ycor() + 1
        self.teleport(new_xcor, new_ycor)