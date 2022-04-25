from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(fun=snake.turn_up, key='Up')
screen.onkey(fun=snake.turn_down, key='Down')
screen.onkey(fun=snake.turn_left, key='Left')
screen.onkey(fun=snake.turn_right, key='Right')


game_is_on = True
food = Food()
scoreboard = Scoreboard()
while game_is_on:
    screen.update()
    if snake.head.distance(food) < 15:
        food.change_position()
        scoreboard.increase_score()
        snake.extend()

    time.sleep(0.1)
    snake.move()

# detecting collision
    if snake.head.xcor() > 280 or snake.head.ycor() > 295 or snake.head.xcor() < -300 or snake.head.ycor() < -280:
        scoreboard.restart()
        snake.restart()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.restart()
            snake.restart()

screen.exitonclick()
