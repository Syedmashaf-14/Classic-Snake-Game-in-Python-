from turtle import Turtle, Screen
initial_pos = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE=20
class Snake:

    def __init__(self):
        self.segment=[]
        self.create_snake()

    def create_snake(self):
        for i in initial_pos:
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(i)
            self.segment.append(new_turtle)


    def snake_grow(self):
        x_pos=self.segment[len(self.segment)-1].xcor()
        y_pos = self.segment[len(self.segment) - 1].ycor()
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(x_pos,y_pos)
        self.segment.append(new_turtle)

    def move_up(self):
        self.segment[0].setheading(90)

    def move_down(self):
        self.segment[0].setheading(270)

    def move_left(self):
        self.segment[0].setheading(180)

    def move_right(self):
        self.segment[0].setheading(0)

    def snake_linkage(self):
         for seg in range(len(self.segment) - 1, 0, -1):
            x_axis = self.segment[seg - 1].xcor()
            y_axis = self.segment[seg - 1].ycor()
            self.segment[seg].goto(x_axis, y_axis)
         self.segment[0].forward(DISTANCE)

    def snake_position_x(self):
        x_axis=self.segment[0].xcor()
        return x_axis

    def snake_position_y(self):
        y_axis = self.segment[0].ycor()
        return y_axis



