import time
from turtle import Screen, Turtle

screen = Screen()


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create()
        self.x_move = 10
        self.y_move = 10

    def create(self):
        self.shape("circle")
        self.color("white")

    def move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.teleport(new_xcor, new_ycor)

    def bounce(self):
        self.y_move *=-1




