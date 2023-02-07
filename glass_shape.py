import turtle

def draw_glass():
    turtle.speed(10)
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.circle(100)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.circle(100, 180)
    turtle.penup()
    turtle.goto(-50, -100)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(100)
    turtle.penup()
    turtle.goto(50, -100)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(100)

draw_glass()
turtle.done()