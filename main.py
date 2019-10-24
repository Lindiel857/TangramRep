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
    turtle.rt(90)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    turtle.done()
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
    turtle.done()
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
    turtle.done()
    pass

def main():
    # TODO: (Anna) Figure 1
    pass

    # TODO: (Anna) Figure 2
    pass

    # TODO: (Daria) Figure 3
    pass

    # TODO: (Daria) Figure 4
    pass

    # TODO: (Timothey) Figure 5
    pass

    # TODO: (Timothey) Figure 6
    pass

    # TODO: (Baba Yaga) Figure 7
    pass

if __name__ == '__main__':
    main()
