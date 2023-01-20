# import colorgram
#
# colors = colorgram.extract('hirst.jpg', 30)
#
# color_list = []
# for item in colors:
#     r = item.rgb.r
#     g = item.rgb.g
#     b = item.rgb.b
#     color_list.append((r, g, b))
#
# print(color_list)

import turtle as t
import random
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

colors_list = [(28, 107, 145), (233, 151, 73), (12, 170, 208), (5, 57, 98), (148, 76, 27), (28, 136, 75), (216, 131, 162), (141, 31, 49), (215, 94, 124), (206, 156, 19), (5, 104, 66), (217, 210, 10), (2, 70, 138), (239, 212, 80), (15, 50, 45), (152, 189, 174)]
tim.setposition(-300, -300)

for i in range(30):
    tim.setposition(-300, -300+20*i)
    tim.dot(10, random.choice(colors_list))
    for _ in range(30):
        tim.setheading(0)
        tim.forward(20)
        tim.dot(10, random.choice(colors_list))


screen = t.Screen()
screen.exitonclick()
