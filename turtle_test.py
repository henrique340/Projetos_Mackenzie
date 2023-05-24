import turtle
from time import sleep
tar = turtle.Turtle()

# triângulo rosa
tar.fillcolor('#C0504D')
tar.begin_fill()
for c in range(3):
    tar.forward(100)
    tar.left(120)
tar.end_fill()

# posição
tar.penup()
tar.setposition(100, 0)
tar.pendown()

# quadrilátero vermelho
tar.fillcolor('#C00000')
tar.begin_fill()
tar.forward(300)
tar.left(120)
tar.forward(100)
tar.left(60)
tar.forward(300)
tar.left(120)
tar.forward(100)
tar.left(60)
tar.end_fill()

# posição
tar.penup()
tar.setposition(0,0)

# quadrado laranja
tar.fillcolor('#FF8200')
tar.begin_fill()
for c in range(4):
    tar.forward(100)
    tar.right(90)
tar.end_fill()

# posição
tar.setposition(100, 0)

# retângulo amarelo
tar.fillcolor('#FFC000')
tar.begin_fill()
for c in range(2):
    tar.forward(300)
    tar.right(90)
    tar.forward(100)
    tar.right(90)
tar.end_fill()

# posição
tar.penup()
tar.setposition(100/3, -100/3)
tar.pendown()

# retângulo preto
tar.fillcolor('#000000')
tar.begin_fill()
for c in range(2):
    tar.forward(100/3)
    tar.right(90)
    tar.forward(200/3)
    tar.right(90)
tar.end_fill()

# posição
tar.penup()
tar.setposition(100+(100/3), -100/4)
tar.pendown()

# retângulo preto 1
tar.fillcolor('#000000')
tar.begin_fill()
for c in range(2):
    tar.forward(100)
    tar.right(90)
    tar.forward(100/3)
    tar.right(90)
tar.end_fill()


# posição
tar.penup()
tar.setposition(250+(100/3), -100/4)
tar.pendown()

# retângulo preto 2
tar.fillcolor('#000000')
tar.begin_fill()
for c in range(2):
    tar.forward(100)
    tar.right(90)
    tar.forward(100/3)
    tar.right(90)
tar.end_fill()
sleep(4)