from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()
def movement():
    screen.listen()
    screen.onkey(key="Up", fun=snake.move_up)
    screen.onkey(key="Down", fun=snake.move_down)
    screen.onkey(key="Left", fun=snake.move_left)
    screen.onkey(key="Right", fun=snake.move_right)

movement()
game_exit=False
count=0
while not game_exit:

    screen.update()
    time.sleep(0.1)

    snake.snake_linkage()

    if snake.segment[0].distance(food.food)<15:
        food.refresh()
        scoreboard.increase_score()
        screen.update()
        snake.snake_grow()

    if (
            snake.segment[0].xcor() > 280 or snake.segment[0].xcor() < -280 or
            snake.segment[0].ycor() > 280 or snake.segment[0].ycor() < -280
    ):
        scoreboard.game_over()
        game_exit = True

    else:
        for i in range(1,len(snake.segment)):
            if snake.segment[0].distance(snake.segment[i]) < 15:
                scoreboard.game_over()
                game_exit = True
                break;




screen.exitonclick()
