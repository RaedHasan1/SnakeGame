from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.penup()
        self.shapesize(0.00000001)
        self.goto(0, 210)
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        self.write(f"score: {self.score} | high score: {self.high_score}", align="center", font=("david", 24, "normal"))

    def snake_eat(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update()
