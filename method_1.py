# from turtle import Turtle, Screen
#
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("Snake Game")
#
# x = 0
#
# for _ in range(3):
#     turtle = Turtle(shape="square")
#     turtle.color("white")
#     turtle.setpos(x, 0)
#     x -= 20
#
#
#
#
#
# screen.exitonclick()



#Method 2

from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
positions = [(0, 0), (-20, 0), (-40, 0)]



segments = []
for position in positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.setpos(position)
    segments.append(new_segment)

left = True
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for segment in range(len(segments) - 1, 0, -1):
        new_x = segments[segment - 1].xcor()
        new_y = segments[segment - 1].ycor()
        segments[segment].goto(new_x, new_y)
    segments[0].forward(20)

    # for segment in range(0, len(segments) - 1, 1):
    #     new_x = segments[segment].xcor()
    #     new_y = segments[segment].ycor()
    #     segments[segment + 1].goto(new_x, new_y)
    # segments[0].forward(20)
    # if left:
    #     segments[0].left(90)
    #     left = False
screen.exitonclick()
