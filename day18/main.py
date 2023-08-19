from turtle import Turtle, Screen
import random

colours = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]


timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
directions = [0, 98, 180, 270]
# timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
# for _ in range (15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#
# for shape_side_n in range(3,11):
#     timmy_the_turtle.color(random.choice(colours))
#     draw_shape(shape_side_n)


# for _ in range(200):
#     timmy_the_turtle.color(random.choice(colours))
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(directions))


for _ in range(100):
    timmy_the_turtle.color(random.choice(colours))
    timmy_the_turtle.circle(100)
    timmy_the_turtle.setheading(timmy_the_turtle.heading() + 10)





















screen = Screen()
screen.exitonclick()