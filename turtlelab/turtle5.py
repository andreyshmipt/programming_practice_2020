import turtle
N=10
turtle.shape('turtle')
for i in range(10):
    for s in range(4):
        turtle.forward((i+1)*10)
        turtle.left(90)
    turtle.right(90)
    turtle.penup()
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.right(180)
    turtle.pendown()