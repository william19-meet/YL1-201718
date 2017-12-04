from turtle import *
import random


class Ball(turtle):
    def __init__(self,radius,color,speed):
        turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius)
        self.color(color)
        self.speed(speed)


    ball1 = Ball(5,"Red",5)
    ball2 = Ball(10, "green", 5)


    def check_collision(ball1,ball2):
        if Ball1.shapesize() <= Ball2.shapesize():
            exit()
