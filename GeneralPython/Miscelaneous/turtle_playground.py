import turtle
pen = turtle.Pen()
wn = turtle.Screen()
wn.bgcolor('black')
pen.pencolor('white')
pen.speed(5)


def rectangle(x, y):
    pen.setheading(0)
    for _ in range(2):
        pen.forward(x)
        pen.left(90)
        pen.forward(y)
        pen.left(90)

def paralelepipedo(x, y):
    pen.setheading(0)
    pen.left(45)
    pen.forward(x)
    pen.left(45)
    pen.forward(y)
    pen.setheading(225)
    pen.forward(x)
    pen.setheading(270)
    pen.forward(y)

def make_house(largura, altura, comprimento, fill_front=False, fill_back=False, color_floor=False, color_roof=False):
    largura = largura*10
    altura = altura*10
    comprimento = comprimento*10
    pen.up()
    pen.setpos(-(largura/2)-(comprimento/3), -(altura/2)-(comprimento/3))
    pen.down()
    initial = pen.pos()

    if color_floor:
        pen.fillcolor('blue')
        pen.begin_fill()
        pen.setheading(45)
        pen.forward(comprimento)
        pen.setheading(0)
        pen.forward(largura)
        pen.setheading(225)
        pen.forward(comprimento)
        pen.setheading(180)
        pen.forward(largura)
        pen.end_fill()
    
    pen.setheading(0)

    if fill_back:
        pen.fillcolor('green')
        pen.begin_fill()
        paralelepipedo(comprimento, altura)
        pen.end_fill()
    else:
        paralelepipedo(comprimento, altura)

    pen.setpos(initial)
    pen.setheading(45)
    pen.forward(comprimento)
    if fill_back:
        pen.fillcolor('green')
        pen.begin_fill()
        rectangle(largura, altura)
        pen.end_fill()
    else:
        rectangle(largura, altura)

    pen.up()
    pen.setpos(initial)
    pen.down()
    if fill_front:
        pen.fillcolor('green')
        pen.begin_fill()
        rectangle(largura, altura)
        pen.end_fill()
    else:
        rectangle(largura, altura)

    pen.up()
    pen.setpos(initial)
    pen.setheading(0)
    pen.forward(largura)
    pen.down()
    if fill_front:
        pen.fillcolor('green')
        pen.begin_fill()
        paralelepipedo(comprimento, altura)
        pen.end_fill()
    else:
        paralelepipedo(comprimento, altura)

    if color_roof:
        pen.up()
        pen.setpos(initial)
        pen.setheading(90)
        pen.forward(altura)
        pen.fillcolor('blue')
        pen.begin_fill()
        pen.setheading(45)
        pen.forward(comprimento)
        pen.setheading(0)
        pen.forward(largura)
        pen.setheading(225)
        pen.forward(comprimento)
        pen.setheading(180)
        pen.forward(largura)
        pen.end_fill() 

make_house(20,10,30, fill_back=True, color_floor=True, fill_front=True)
pen.hideturtle()
wn.mainloop()