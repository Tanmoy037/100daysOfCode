from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

new_snake = []
x = 0
y = 0
for _ in range(0,3):
    turtle_new = Turtle()
    turtle_new.color("white")
    turtle_new.shape("square")
    turtle_new.penup()
    turtle_new.goto(x, y)
    new_snake.append(turtle_new)
    x -= 20
    
game_is_on = True
while game_is_on:
    for snake in new_snake:
        snake.forward(20)




















screen.exitonclick()
