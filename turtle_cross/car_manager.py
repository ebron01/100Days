from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setposition(280, random.randrange(-250, 250))
            self.cars.append(new_car)
            
    def move(self):
        for car in self.cars:
            car.forward(self.car_speed) 
        
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
    