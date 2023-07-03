import random
from turtle import Turtle

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
colors = ["red", "green", "brown", "blue", "yellow", "purple", "orange",
          "olive", "cyan", "antique white"]


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.body = []
        self.create_snake()
        self.snake_head = self.body[0]

    def create_snake(self):
        for position in INITIAL_POSITIONS:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.goto(position)
            self.body.append(new_segment)

    def update_move(self):
        for segment in range(len(self.body) - 1, 0, -1):
            new_x = self.body[segment - 1].xcor()
            new_y = self.body[segment - 1].ycor()
            self.body[segment].goto(new_x, new_y)
            self.body[segment].color(colors[random.randint(0, len(colors) - 1)])
            self.snake_head.color(colors[random.randint(0, len(colors) - 1)])
        self.snake_head.forward(MOVE_DIS)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
        else:
            pass

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
        else:
            pass

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
        else:
            pass

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
        else:
            pass

    def snake_eat(self):
        new_segment = Turtle("square")
        new_segment.penup()
        self.body.append(new_segment)

    def snake_reset(self):
        for segment in self.body:
            segment.goto(800, 800)
        self.body.clear()
        self.create_snake()
        self.snake_head = self.body[0]
