from turtle import Turtle, Screen
from time import sleep

STARTING_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
TURTLE_WIDTH = 0.5
TURTLE_HEIGHT = 0.5

screen=Screen()

class Snake(Turtle):
    def __init__(self):
        # my_snake = []
        super().__init__()
        self.my_snake = []
        self.start_snake()
        self.head = self.my_snake[0]
        self.head.shape('turtle')

    def start_snake(self):
        for position in STARTING_POSITIONS:
            self.add_square(position)

    def add_square(self, position):
        new_segment = Turtle("square")
        new_segment.speed('fastest')
        new_segment.shapesize(TURTLE_HEIGHT, TURTLE_WIDTH)
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.my_snake.append(new_segment)

    def extend_snake(self):
        for i in range(1):
            self.add_square(self.my_snake[-1].position())

    def move_snake(self):
        for square in range(len(self.my_snake) - 1, 0, -1):
            new_x = self.my_snake[square - 1].xcor()
            new_y = self.my_snake[square - 1].ycor()
            self.my_snake[square].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)


    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)


    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)

    # global coordinates

    def snake_position(self):
        coordinates = []
        for segment in self.my_snake:
            # print(segment)
            # print(type(segment))
            # print(segment.pos())
            coordinates.append(segment.pos())
        # print(coordinates)
        return coordinates


