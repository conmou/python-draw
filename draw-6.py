import turtle

color = ["yellow", "white","yellow", "white","yellow", "white"]
turtle.bgcolor("black")
t = turtle.Pen()
t.speed(40)
t.pensize(0.1)
# squary = turtle.Turtle()
# squary.speed(200)

for i in range(360):
    t.pencolor(color[i%6])
    t.width(i/100 + 1)
    t.forward(i)
    t.left(59)