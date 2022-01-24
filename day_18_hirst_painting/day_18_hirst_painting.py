# import colorgram
import turtle as turtle_module
import random
# Used to extract colours from an image
# rgb_colours = []
# colours = colorgram.extract("day_18_hirst_painting/image.jpg", 30)
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r,g,b)
#     rgb_colours.append(new_colour)
# print(rgb_colours)

screen = turtle_module.Screen()
screen.title("Rainbow colours - Unknown Turtle (2022)")
turtle_module.colormode(255)
stephen = turtle_module.Turtle()
stephen.shape("turtle")
stephen.speed("fastest")
colour_list =[(248, 231, 27), (202, 12, 30), (238, 244, 250), (35, 91, 186), (232, 229, 4), (232, 149, 48), (197, 68, 22), (212, 13, 9), (35, 31, 152), (49, 220, 60), (241, 46, 151), (20, 22, 53), (14, 208, 224), (75, 9, 53), (17, 154, 18), (55, 26, 13), (80, 193, 223), (219, 23, 116), (232, 159, 8), (241, 64, 24), (221, 138, 191), (96, 75, 10), (247, 11, 9), (83, 238, 162), (11, 96, 63), (5, 35, 33), (89, 208, 147)]

stephen.penup()
stephen.hideturtle()
stephen.setheading(225)
stephen.forward(300)
stephen.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    stephen.dot(20, random.choice(colour_list))
    stephen.forward(50)
    if dot_count % 10 == 0:
        stephen.setheading(90)
        stephen.forward(50)
        stephen.setheading(180)
        stephen.forward(500)
        stephen.setheading(0)

screen.exitonclick()
