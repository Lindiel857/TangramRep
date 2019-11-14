import turtle

def square(x, y, size, colour, angle):
    turtle.pencolor(colour)
    turtle.fillcolor(colour)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.lt(90)
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
    turtle.pencolor(colour)
    turtle.fillcolor(colour)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.lt(90)
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
    turtle.pencolor(colour)
    turtle.fillcolor(colour)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.lt(90)
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

def sleeping_rectangle(x, y, size, colour, angle):
    turtle.pencolor(colour)
    turtle.fillcolor(colour)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.lt(90)
    turtle.rt(angle)
    turtle.begin_fill()
    turtle.fd(size * 1.42)
    turtle.lt(45)
    turtle.fd(size)
    turtle.lt(135)
    turtle.fd(size * 1.42)
    turtle.lt(45)
    turtle.fd(size)
    turtle.lt(135)
    turtle.end_fill()
    turtle.penup()
    turtle.home()

def main():
    turtle.speed(0)
    
    triangle(-500, 200 - 100, 100, 'light slate blue', 0)
    triangle(-600, 300 - 100, 100, 'orange', 90)
    triangle(-500, 300 - 100, 70.5, 'lime green', 0)
    triangle(-535.25, 335.25 - 100, 50, 'yellow', 315)
    triangle(-500, 370.5 - 100, 50, 'blue', 45)
    square(-500, 370.5 - 100, 50, 'cyan', 315)
    sleeping_rectangle(-500, 300 - 100, 50, 'purple', 0)

    triangle(-70.5, 0 + 80, 100, 'light slate blue', 45)
    triangle(35.25, 35.35 + 80, 100, 'orange', 315)
    triangle(-35.25, 105.75 + 80, 70.5, 'lime green', 0)
    triangle(-35.25, 105.75 + 80, 50, 'yellow', 135)
    triangle(0, 211.5 + 80, 50, 'blue', 225)
    square(-25, 211.5 + 80, 50, 'cyan', 0)
    sleeping_rectangle(-35.25, 176.25 + 80, 50, 'purple', 90)

    # TODO: (Anna) Figure 3
    pass

    # TODO: (Anna) Figure 4
    pass

    # TODO: (Daria) Figure 5
    pass

    # TODO: (Daria) Figure 6
    pass
    
    turtle.done()

if __name__ == '__main__':
    main()
