from turtle import Turtle
BAR_WIDTH = 5
BAR_LENGTH = 1
MOVE_LENGTH = 20

class Bars(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=BAR_WIDTH, stretch_len=BAR_LENGTH)
        
        
    def left_set_position(self):
        self.goto(-350, 0)
        
    def right_set_position(self):
        self.goto(350, 0)
        
    def up(self):
        ycor = self.ycor()
        xcor = self.xcor()
        self.goto(xcor, ycor + MOVE_LENGTH)
    
    def down(self):    
        ycor = self.ycor()
        xcor = self.xcor()
        self.goto(xcor, ycor - MOVE_LENGTH)