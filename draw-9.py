import turtle

turtle.bgcolor("black")
squary = turtle.Turtle()
squary.speed(25)
for i in range(100):
    for color in ["#77969A", "#B1B479", "#734338"]:
        squary.pencolor(color)
        squary.forward(i)
        squary.left(70)
        squary.right(100)