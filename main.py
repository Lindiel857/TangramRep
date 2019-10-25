import turtle

def square(x, y, size, colour, angle):
    # TODO: (Anna)
    turtle.pencolor(colour)
    turtle.fillcolor(colour)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.rt(angle)
    turtle.begin_fill()
    turtle.fd(size)
    turtle.rt(90)
    turtle.fd(size)
    turtle.rt(90)
    turtle.fd(size)
    turtle.rt(90)
    turtle.fd(size)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    pass

def triangle(x, y, size, colour, angle):
    # TODO: (Timothey)
    turtle.pencolor(colour)
    turtle.fillcolor(colour)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.rt(angle)
    turtle.begin_fill()
    turtle.fd(size)
    turtle.rt(90)
    turtle.fd(size)
    turtle.rt(135)
    turtle.fd(size * 1.42)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    pass

def rectangle(x, y, size, colour, angle):
    # TODO: (Daria)
    turtle.pencolor(colour)
    turtle.fillcolor(colour)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.rt(angle)
    turtle.begin_fill()
    turtle.fd(size * 1.42)
    turtle.rt(45)
    turtle.fd(size)
    turtle.rt(135)
    turtle.fd(size * 1.42)
    turtle.rt(45)
    turtle.fd(size)
    turtle.rt(135)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    pass

def main():
    # TODO: (Anna) Figure 1
    pass

if __name__ == '__main__':
    main()
