from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.small_food()
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, +280)
        random_y = random.randint(-280, +280)
        self.goto(random_x, random_y)

    def small_food(self):
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")

    def bonus(self):
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("red")
        self.speed("fastest")