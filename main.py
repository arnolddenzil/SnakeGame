import time
from turtle import Screen
from snake import Snake
from food import Food
from score_board import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
i = 0
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        i += 1
        if i > 5:
            snake.extend(3)
            score.update_score(5)
            food.small_food()
            i = 0
        else:
            if i == 5:
                food.bonus()
            else:
                food.small_food()
            snake.extend(1)
            score.update_score(1)

    # detect collision with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
