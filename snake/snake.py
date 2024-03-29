from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20        
SHAPE = "square"

    
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    def add_segment(self, position):
            new_segment = Turtle(shape=SHAPE)
            new_segment.penup()
            new_segment.goto(position)
            new_segment.color("white")
            self.segments.append(new_segment)
    
    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000) 
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        
    def extend(self):
        self.add_segment(self.segments[-1].pos())   
    
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
        #self.segments[0].left(90)
        
    def up(self):
        heading = self.segments[0].heading()
        if heading == 0.0 or heading == 180.0:
            self.segments[0].seth(90)


    
    def down(self):
        heading = self.segments[0].heading()
        if heading == 0.0 or heading == 180.0:
            self.segments[0].seth(270)

        
    def left(self):
        heading = self.segments[0].heading()
        if heading == 90.0 or heading == 270.0:
            self.segments[0].seth(180)


    def right(self):
        heading = self.segments[0].heading()
        if heading == 90.0 or heading == 270.0:
            self.segments[0].seth(0)
        


        
