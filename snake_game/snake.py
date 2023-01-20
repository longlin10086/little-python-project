from turtle import Turtle
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.creat_snake()
        self.head = self.segments[0]

    def creat_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        square = Turtle("square")
        if len(self.segments) > 3:
            square.color(self.segments[-1].color()[0])
        else:
            square.color('pink')
        square.speed("fastest")
        square.penup()
        square.setposition(position)
        self.segments.append(square)

    def snake_again(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.creat_snake()
        self.head = self.segments[0]

    def extend(self):
        position = self.segments[-1].position()
        self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.move()

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.move()

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.move()

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.move()

