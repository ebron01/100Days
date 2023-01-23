from turtle import Turtle
import random
import itertools as it
ANGLES = [x for x in it.chain(range(0, 45), range(135, 180), range(180, 225), range(315,360))]   
MOVE_X = 10
MOVE_Y = 10
BALL_SPEED = 0.05

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        #self.random_start()
        self.move_x= MOVE_X
        self.move_y= MOVE_Y
        self.ball_speed = BALL_SPEED
    def random_start(self):
        self.setheading(random.choice(ANGLES))
    
    def move(self):
        #self.forward(8)
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)
        
    def collision(self):
        # if self.heading() >= 0.0 and self.heading() < 90.0 :
        #     self.goto(self.xcor() + 10, self.ycor() - 10)
        #     #self.left(90)
        #      #self.goto(self.xcor(), 270)
        # elif self.heading() >= 90.0 and self.heading() < 180.0:
        #     self.goto(self.xcor() - 10, self.ycor() - 10)
        #     #self.right(90)
        #      #self.goto(self.xcor(), 270)
        # elif self.heading() > 180.0 and self.heading() < 270.0 :
        #     self.goto(self.xcor() - 10, self.ycor() + 10)
        #     #self.left(90)
        #      #self.goto(self.xcor(), -270)
        # elif self.heading() >= 270.0: 
        #     self.goto(self.xcor() + 10, self.ycor() + 10)
        #     #self.left(90)
        #      #self.goto(self.xcor(), -270)
        self.move_x *= -1
        self.ball_speed *= 0.9
        
    def bounce(self):
        # if self.heading() >= 90.0 and self.heading() < 180.0:
        #     self.right(90)
        # elif self.heading() < 90.0 and self.heading() >= 0.0:
        #     self.left(90)
        # elif self.heading() < 270.0 and self.heading() > 180.0:
        #     self.left(90)
        # elif self.heading() > 270.0: 
        #     self.right(90)
        self.move_y *= -1 
    
    def reset_position(self):
       self.goto(0, 0) 
       self.ball_speed = BALL_SPEED
       self.collision()