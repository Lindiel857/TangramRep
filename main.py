import turtle


def square(x, y, size, colour, angle):
    '''
    Draws a square
    '''
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
    '''
        Draws a triangle
    '''
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
    '''
        Draws a paralellogramm
    '''
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
    '''
        Draws a paralellogramm with another orientation
    '''
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


def figure_1():
    '''
    Draws a flower
    '''
    triangle(-500, 200 - 100, 100, 'light slate blue', 0)
    triangle(-600, 300 - 100, 100, 'orange', 90)
    triangle(-500, 300 - 100, 70.5, 'lime green', 0)
    triangle(-535.25, 335.25 - 100, 50, 'yellow', 315)
    triangle(-500, 370.5 - 100, 50, 'blue', 45)
    square(-500, 370.5 - 100, 50, 'cyan', 315)
    sleeping_rectangle(-500, 300 - 100, 50, 'purple', 0)


def figure_2():
    '''
        Draws a pedestal
    '''
    triangle(-70.5 - 200, 0 + 80, 100, 'light slate blue', 45)
    triangle(35.25 - 200, 35.35 + 80, 100, 'orange', 315)
    triangle(-35.25 - 200, 105.75 + 80, 70.5, 'lime green', 0)
    triangle(-35.25 - 200, 105.75 + 80, 50, 'yellow', 135)
    triangle(0 - 200, 211.5 + 80, 50, 'blue', 225)
    square(-25 - 200, 211.5 + 80, 50, 'cyan', 0)
    sleeping_rectangle(-35.25 - 200, 176.25 + 80, 50, 'purple', 90)


def figure_3():
    '''
        Draws a bridge
    '''
    triangle(0 - 500, 100 - 300, 100, 'light slate blue', 180)
    triangle(250 - 500, 0 - 300, 100, 'orange', 270)
    triangle(0 - 500, 100 - 300, 70.5, 'lime green', 135)
    triangle(50 - 500, 100 - 300, 50, 'yellow', 90)
    triangle(100 - 500, 50 - 300, 50, 'blue', 90)
    square(100 - 500, 50 - 300, 50, 'cyan', 0)
    sleeping_rectangle(0 - 500, 100 - 300, 50, 'purple', 135)


def figure_4():
    '''
        Draws a bowl
    '''
    triangle(-70.5 - 100, 0 - 300, 100, 'light slate blue', 45)
    triangle(-50 - 100, 20.5 - 300, 100, 'orange', 0)
    triangle(100 - 100, 70.5 - 300, 70.5, 'lime green', 225)
    triangle(-100 - 100, 70.5 - 300, 50, 'yellow', 90)
    triangle(100 - 100, 120.5 - 300, 50, 'blue', 180)
    square(-100 - 100, 70.5 - 300, 50, 'cyan', 0)
    rectangle(0 - 100, 70.5 - 300, 50, 'purple', 45)


def figure_5():
    '''
        Draws a swan
    '''
    triangle(100 + 400, 0 - 300, 100, 'light slate blue', 270)
    triangle(0 + 400, 100 - 300, 100, 'orange', 90)
    triangle(0 + 400, 0 - 300, 70.5, 'lime green', 315)
    triangle(29.5 + 400, 100 - 300, 50, 'yellow', 45)
    triangle(29.5 + 400, 191 - 300, 50, 'blue', 0)
    square(29.5 + 400, 100 - 300, 50, 'cyan', 315)
    rectangle(-5.75 + 400, 135.25 - 300, 50, 'purple', 0)


def figure_6():
    '''
        Draws a rectangle
    '''
    triangle(0 + 100, 0 - 300, 100, 'light slate blue', 0)
    triangle(100 + 100, 100 - 300, 100, 'orange', 180)
    triangle(0 + 100, 100 - 300, 70.5, 'lime green', 45)
    triangle(0 + 100, 100 - 300, 50, 'yellow', 0)
    triangle(50 + 100, 200 - 300, 50, 'blue', 90)
    square(0 + 100, 150 - 300, 50, 'cyan', 0)
    rectangle(100 + 100, 100 - 300, 50, 'purple', 315)


def figure_7():
    '''
        Draws a crow
    '''
    triangle(70.5 + 100, 0 + 200, 100, 'light slate blue', 180)
    triangle(-14.75 + 100, 85.25 + 200, 100, 'orange', 90)
    triangle(0 + 100, 70.5 + 200, 70.5, 'lime green', 180)
    triangle(50 + 100, 85.25 + 200, 50, 'yellow', 270)
    triangle(0 + 100, 70.5 + 200, 50, 'blue', 135)
    square(0 + 100, 0 + 200, 50, 'cyan', 45)
    rectangle(120.5 + 100, 85.25 + 200, 50, 'purple', 270)


def figure_8():
    '''
        Draws another swan
    '''
    triangle(120.5 + 400, -20.5 + 150, 100, 'light slate blue', 315)
    triangle(120.5 + 400, 120.5 + 150, 100, 'orange', 135)
    triangle(0 + 400, 0 + 150, 70.5, 'lime green', 45)
    triangle(226.25 + 400, 85.25 + 150, 50, 'yellow', 225)
    triangle(-35.25 + 400, 105.75 + 150, 50, 'blue', 135)
    square(-35.25 + 400, 105.75 + 150, 50, 'cyan', 45)
    rectangle(0 + 400, 0 + 150, 50, 'purple', 0)


def main():
    turtle.ht()
    turtle.speed(0)
    figure_1()
    figure_2()
    figure_3()
    figure_4()
    figure_5()
    figure_6()
    figure_7()
    figure_8()
    turtle.done()


if __name__ == '__main__':
    main()
