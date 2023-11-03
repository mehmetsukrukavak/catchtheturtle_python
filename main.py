import turtle

FONT = ('Arial', 30, 'normal')
screen = turtle.Screen()

screen.bgcolor("Light Blue")
screen.title("Catch The Turtle")

grid_size = 10
#score turtle
def setup_score_turtle():
    score_turtle = turtle.Turtle()
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

    t.goto(x * grid_size ,y * grid_size)

setup_score_turtle()

x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]

for x in x_coordinates:
    for y in y_coordinates:
        make_turtle(x,y)

turtle.mainloop()