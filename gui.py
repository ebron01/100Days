from turtle import Turtle, Screen

tim = Turtle()

def move_forwards():
    tim.forward(10)

def move_backwards(): 
    tim.backward(10)

def move_Cclockwise():
    tim.circle(120, 30)
    
def move_clockwise():
    tim.circle(120, -30)
    
def clear():
    screen.resetscreen()
    
    
screen = Screen()
screen.listen()
screen.onkey(key="W", fun=move_forwards)
screen.onkey(key="S", fun=move_backwards)
screen.onkey(key="A", fun=move_Cclockwise)
screen.onkey(key="D", fun=move_clockwise)
screen.onkey(key="C", fun=clear)
screen.exitonclick()