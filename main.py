import turtle
import random
FONT = ('Arial', 30, 'normal')
screen = turtle.Screen()

screen.bgcolor("Light Blue")
screen.title("Catch The Turtle")

grid_size = 10
score = 0
#turtle list
turtle_list = []
#score turtle
score_turtle = turtle.Turtle()
def setup_score_turtle():

    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.9
    score_turtle.setpos(0,  y)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)

def make_turtle(x, y):
    t = turtle.Turtle()
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    def handle_click(x,y):
        global  score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg="Score: {}".format(score), move=False, align="center", font=FONT)

    t.onclick(handle_click)
    t.goto(x * grid_size ,y * grid_size)
    turtle_list.append(t)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtle_randomly():
    hide_turtles()
    random.choice(turtle_list).showturtle()
    screen.ontimer(show_turtle_randomly, 500)


x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]
def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

turtle.tracer(0)

setup_score_turtle()
setup_turtles()
hide_turtles()
show_turtle_randomly()
turtle.tracer(1)

turtle.mainloop()