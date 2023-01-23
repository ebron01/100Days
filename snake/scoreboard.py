from turtle import Turtle
ALIGNMENT = "center"
FONT = "Arial, 12"

class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.setposition(0, 270)
        self.score = 0
        with open("score.txt") as f:
            self.high_score = int(f.read())
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()

        self.write((f"Score = {self.score} High score = {self.high_score}"), False, align=ALIGNMENT, font=FONT) 
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", "w") as f:
                f.write(str(self.high_score))
                
        self.score = 0 
        self.update_scoreboard()
    
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    

    # def write_gameover(self):
    #     self.setposition(0,0)
    #     self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)