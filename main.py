import turtle as t
from random import randint

def create_racers():
    racers = []
    y_cor = -120
    screen.tracer(0)
    for color in colors:
        racer = t.Turtle(shape="turtle")
        racer.penup()
        racer.color(color)
        racer.goto(x=-230, y=y_cor)
        racers.append(racer)
        y_cor += 60
    screen.tracer(1)
    return racers

def get_user_bet():
    prompt = screen.textinput(title="Make Your Bet", prompt="Which turtle do you think will win? Enter a color:").lower()

    while prompt not in colors:
        prompt = screen.textinput(title="Invalid Input", prompt="Your choice of color doesn't exist. Enter a valid color:").lower()

    return prompt

def display_result(racer):
    output.penup()
    if racer == user_bet:
        output.write(arg=f"You Won, The {racer} turtle is The Winner", move=False, align="center", font=("Arial", 18, "normal"))
    else:
        output.write(arg=f"You Lost, The {racer} turtle is The Winner", move=False, align="center", font=("Arial", 18, "normal"))

colors = ["red", "blue", "green", "yellow", "orange"]

output = t.Turtle(visible=False)
screen = t.Screen()
screen.title("Welcome to The Turtle Race")
screen.setup(500, 400)

racer_list = create_racers()
user_bet = get_user_bet()


race_on = True
finish_line = 230

while race_on:
    for racer in racer_list:
        if racer.xcor() > finish_line:
            race_on = False
            winner = racer.pencolor()
            display_result(winner)
        random_distance = randint(0,10)
        racer.forward(random_distance)

screen.exitonclick()