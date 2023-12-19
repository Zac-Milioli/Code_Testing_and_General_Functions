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

def make_house(largura, altura, comprimento):
    largura = largura*10
    altura = altura*10
    comprimento = comprimento*10
    initial = pen.pos()

    pen.fillcolor('blue')
    pen.begin_fill()
    paralelepipedo(comprimento, altura)
    pen.end_fill()

    rectangle(largura, altura)

    pen.setpos(initial)
    pen.setheading(45)
    pen.forward(comprimento)

    pen.fillcolor('blue')
    pen.begin_fill()
    rectangle(largura, altura)
    pen.end_fill()

    pen.up()
    pen.setpos(largura, 0)
    pen.down()
    paralelepipedo(comprimento, altura)

make_house(10,5,10)

wn.mainloop()