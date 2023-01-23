from turtle import Turtle, Screen
from scoreboard import Scoreboard
from bars import Bars
from ball import Ball
import time

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGTH)
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()
left_bar = Bars()
left_bar.left_set_position()       
right_bar = Bars()
right_bar.right_set_position()   

ball = Ball()


game_is_on = True
screen.listen()
screen.onkey(left_bar.up, "w")
screen.onkey(left_bar.down, "s")
screen.update()
screen.onkey(right_bar.up, "Up")
screen.onkey(right_bar.down, "Down")
#print(ball.heading())

while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()
    # if ball.ycor() >= ((SCREEN_HEIGTH / 2) - 30) or ball.ycor() <= -((SCREEN_HEIGTH / 2) - 30):
    if ball.distance(right_bar) < 50 and ball.xcor() > 320.0: 
        ball.collision()
        scoreboard.upd_score_right()
    elif ball.distance(left_bar) < 50 and ball.xcor() < -320.0:
        ball.collision()
        scoreboard.upd_score_left()
    # if left_bar.distance(ball.pos()) < 30.0 or right_bar.distance(ball.pos()) < 20.0:      
    if ball.ycor() > 280.0 or ball.ycor() < -280.0:
        ball.bounce()
        
    if ball.xcor() < -380:
        ball.reset_position()
        left_bar.left_set_position()
        right_bar.right_set_position()
        scoreboard.game_over()
        
    if ball.xcor() > 380:
        # game_is_on = False
        ball.reset_position()
        left_bar.left_set_position()
        right_bar.right_set_position()
        scoreboard.game_over()
    
    
# screen.update()
screen.exitonclick()