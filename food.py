from turtle import Turtle
from snake import Snake
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('yellow')
        self.speed('fastest')
        self.refresh()        # print(Snake.snake_position(self))


    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
        return random_x, random_y
