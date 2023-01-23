from turtle import Turtle, Screen
import random
colors = ["red", "blue", "black", "green", "yellow", "cyan"]
names = ["tim", "tom", "tam", "tum", "tem", "nim"]
position_y = [-75, -50, -25, 0, 25, 50]

def create():
    for i in range(len(colors)):
        names[i] = Turtle(shape="turtle")
        names[i].color(colors[i])
        names[i].penup()
        names[i].goto(x=-230, y= position_y[i])
        

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="RACE", prompt="Guess which player will win the race:")
flag = True

create()
while flag:
    for i in range(len(colors)):
        names[i].forward(random.randint(0, 10))
        if names[i].position()[0] > 240:
            flag = False
            if user_bet == names[i].color():
                print("you've won!")
            else: 
                print(f"you've lost!, winning turtle {names[i].pencolor()}")
            screen.bye()
            break
