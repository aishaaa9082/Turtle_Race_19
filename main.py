from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange","green","blue","yellow","purple"]
pos = [-78,-48,-10,20,50,80]
race = False
all_turtles = []

for turtle in range(0, 6):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(-230, pos[turtle])
    all_turtles.append(new_turtle)

if user_bet:
    race = True

while race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            wincolor = turtle.pencolor()
            if wincolor == user_bet:
                print("You won! the {wincolor} turtle is the winner.")
            else:
                print(f"You lost. The {wincolor} turtle is the winner.")
            race= False
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)



screen.exitonclick()