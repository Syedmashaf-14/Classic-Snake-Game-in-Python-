from turtle import Turtle
import random

class Food:
    def __init__(self):
        self.food = Turtle(shape="circle")
        self.food.penup()
        self.food.color("blue")
        self.food.shapesize(1)
        self.refresh()

    def refresh(self):
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        self.food.goto(x, y)
