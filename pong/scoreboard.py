from turtle import Turtle

DASH_LENGHT = 10
HEIGHT = 600
SCORE_LEFT = 0 
SCORE_RIGHT = 0 
FONT = "Arial, 16"
CENTER="center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fast")
        
        # self.setpos(0,300)
        # self.setheading(270)
        # flag = True
        # for index in range(int(HEIGHT / DASH_LENGHT)):
        #     if flag:
        #         self.pendown()
        #         self.forward(DASH_LENGHT)
        #         flag = False
        #     else:
        #         self.penup()
        #         self.forward(DASH_LENGHT)
        #         flag = True
        self.score_left = SCORE_LEFT
        self.score_right = SCORE_RIGHT   
        self.write_score()
             
    def write_score(self):
        self.clear()
        self.setposition(-100, 250)
        self.write(f"{self.score_left}", font=FONT)
        self.setposition(100, 250)
        self.write(f"{self.score_right}", font=FONT)

    def upd_score_left(self) :
        self.score_left += 1
        self.write_score()  
    
    def upd_score_right(self) :
        self.score_right += 1 
        self.write_score() 
        
    def game_over(self):
        self.setposition(0, 0)
        self.score_left = SCORE_LEFT
        self.score_right = SCORE_RIGHT
        self.write_score()
        # self.write("GAME OVER", align=CENTER, font=FONT)