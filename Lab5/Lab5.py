from turtle import Turtle,colormode
import turtle
import random

##colormode(255)
##class Square(Turtle):
##        def __init__(self,size):
##                Turtle.__init__(self)
##                self.shapesize(size)
##                self.shape("square")
##        def random_color(self):
##                
##                r = random.randint(0,256)
##                b = random.randint(0,256)
##                g = random.randint(0,256)
##                self.color(r,b,g)       
##
##square = Square(10)
##square.random_color()


class Hexagon(Turtle):
        def __init__(self,size):
                Turtle.__init__(self)
                self.begin_poly()
                for i in range(6):
                        self.forward(size)
                        self.left(360/6)
                self.end_poly()
                turtle.register_shape("hexagon",self.get_poly())
                self.shape("hexagon")
                self.shapesize(size)
                
                


hexagon = Hexagon(random.randint(0,256))

turtle.mainloop()





