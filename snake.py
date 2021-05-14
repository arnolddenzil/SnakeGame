from turtle import Turtle
STARTING_POSITION = [(0,0), (-20,0), (-40,0), (-60,0), (-80,0)]
MOVE_DISTANCE = 20
# SNAKE_STARTING_LENGTH = 10


class Snake:
    def __init__(self):
        self.segment = []
        self.starting_snake()
        self.head = self.segment[0]

    def starting_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.color("green")
        snake.up()
        snake.goto(position)
        self.segment.append(snake)

    def extend(self, count):
        for _ in range(count):
            self.add_segment(self.segment[-1].position())

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.move_head()

    def move_head(self):
        x_pos = self.head.xcor()
        y_pos = self.head.ycor()
        if x_pos > 300:
            self.head.goto(-300, y_pos)
        elif x_pos < -300:
            self.head.goto(300, y_pos)
        elif y_pos > 300:
            self.head.goto(x_pos, -300)
        elif y_pos < -300:
            self.head.goto(x_pos, 300)
        else:
            self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
