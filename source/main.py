from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time

screen = Screen()
screen.title("SNAKE GAME!")
screen.setup(width=500, height=500)
screen.bgcolor("black")

screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.update_move()

    if snake.snake_head.distance(food) < 15:
        food.food_position()
        snake.snake_eat()
        score.snake_eat()

    if snake.snake_head.xcor() > 240 or snake.snake_head.xcor() < -240 or snake.snake_head.ycor() > 240 \
            or snake.snake_head.ycor() < -240:
        score.reset()
        snake.snake_reset()

    for segment in snake.body[1:]:
        if snake.snake_head.distance(segment) < 10:
            score.reset()
            snake.snake_reset()

screen.exitonclick()
