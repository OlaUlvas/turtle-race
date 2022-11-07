from turtle import Turtle, Screen
import random

#numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
#random_color = "#"
is_race_on = False


#colors = ["CornflowerBlue", "DarkSeaGreen2", "burlywood2", "burlywood4", "aquamarine4", "bisque3"]
colors = ["green", "lightgreen", "yellow", "lightblue", "gray", "red"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which color will win? ")

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner.")
            else:
                print(f"You've lost! The {winning_color} is the winner.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()

