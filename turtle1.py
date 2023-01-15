import turtle
colors = [ "red", "green", "yellow", "blue", "orange"]
t = turtle.Pen()
turtle.bgcolor("black")

for i in range(250):
    t.pencolor(colors[i%5])
    # t.width(i/100+1)
    t.forward(i)
    t.left(72)

turtle.exitonclick()
