import colorgram
from turtle import *
import random
colormode(255)
rgb_colors = [(254, 250, 220), (187, 8, 78), (244, 220, 58), (231, 134, 50), (232, 84, 10), (141, 48, 132), (142, 190, 19), (205, 135, 164), (234, 72, 100), (6, 160, 228), (0, 144, 229), (85, 190, 225), (245, 162, 163), (206, 233, 222), (157, 216, 223)]
tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
# colors = colorgram.extract('dot.png', 30)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dot = 100
for dot_count in range(1, number_of_dot + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

