import turtle as turtle_module
import random

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('hirst.jpg', 100)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_list = [(242, 243, 245), (230, 228, 224), (236, 241, 238), (241, 236, 240), (198, 159, 116), (70, 92, 129),
              (147, 85, 53),
              (218, 210, 116), (138, 160, 191), (178, 160, 38), (184, 146, 164), (28, 32, 46), (58, 34, 23),
              (120, 70, 93),
              (139, 175, 154), (77, 115, 79), (143, 25, 16), (186, 97, 82), (61, 31, 42), (121, 27, 41), (45, 58, 94),
              (177, 96, 114), (102, 119, 170), (34, 52, 45), (100, 160, 85), (214, 175, 192), (216, 181, 173),
              (160, 209, 191),
              (67, 86, 23), (219, 206, 8), (181, 186, 213), (46, 72, 57), (168, 201, 212), (100, 137, 144)]

turtle_module.colormode(255)
timmy = turtle_module.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(30, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
