import turtle

color = ["white", "red", "orange", "yellow", "green", "blue"]
turtle.bgcolor("black")
# t = turtle.Pen()
turtle.speed(0)
# turtle.pensize(0.1)
# squary = turtle.Turtle()
# squary.speed(200)

for i in range(360):
    turtle.pencolor(color[i%6])
    turtle.width(i/5 + 1)
    turtle.forward(i)
    turtle.left(20)