from turtle import Turtle
import random



class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.food_position()

    def food_position(self):
        food_x = random.randint(-240, 240)
        food_y = random.randint(-240, 240)
        self.goto(food_x, food_y)
