import turtle
import random

timmy = turtle.Turtle()

# # This part will get color from an image
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 25)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)


color_list = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223),
              (126, 40, 61), (21, 86, 61), (59, 48, 37), (250, 194, 42), (13, 117, 146),
              (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39), (197, 102, 134),
              (197, 125, 150), (156, 191, 185), (30, 67, 58), (236, 245, 241), (166, 204, 202),
              (62, 26, 45), (145, 165, 181), (6, 79, 111)
              ]

turtle.colormode(255)

# Move downward to center the painting
timmy.penup()
timmy.hideturtle()
timmy.goto(-200, -200)

y = -150

for _ in range(100):
    if _ != 0 and _ % 10 == 0:
        timmy.goto(-200, y)
        y += 50
    timmy.dot(20, random.choice(color_list))
    timmy.penup()
    timmy.forward(50)

screen = turtle.Screen()
screen.exitonclick()
