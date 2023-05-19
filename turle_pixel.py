# bibliotecas
import turtle
from time import sleep

tar = turtle.Turtle()

pixels1 = [[0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
          [0,0,0,1,1,0,0,2,2,0,0,1,1,0,0,0],
          [0,0,1,0,0,0,2,2,2,2,0,0,0,1,0,0],
[0,1,2,2,2,2,2,2,2,2,2,2,2,2,1,0],
[0,1,2,2,2,2,2,2,2,2,2,2,2,2,1,0],
[1,0,2,2,2,2,0,0,0,0,2,2,2,2,0,1],
[1,0,0,2,2,0,0,0,0,0,0,2,2,0,0,1],
[1,0,0,2,2,0,0,0,0,0,0,2,2,0,0,1],
[1,0,2,2,2,2,0,0,0,0,2,2,2,2,0,1],
[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
[1,2,2,2,1,1,1,1,1,1,1,1,2,2,2,1],
[0,1,1,1,3,3,1,3,3,1,3,3,1,1,1,0],
[0,0,1,3,3,3,1,3,3,1,3,3,3,1,0,0],
[0,0,1,3,3,3,3,3,3,3,3,3,3,1,0,0],
[0,0,0,1,3,3,3,3,3,3,3,3,1,0,0,0],
[0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0]
]
# funções

def quadrado():
    for i in range(4):
        tar.forward(5)
        tar.right(90)

def desenhar_Pixels(matriz, cor0, cor1, cor2, cor3):
    tar.pencolor(cor1)
    for i in range(16):
        for j in range(16):
            if matriz[i][j] == 0:
                tar.penup()
                tar.setpos(5 * j, -5 * i)
                tar.pendown()
                tar.pencolor(cor1)
                tar.begin_fill()
                quadrado()
                tar.color(cor0)
                tar.end_fill()
            elif matriz[i][j] == 1:
                tar.penup()
                tar.setpos(5*j, -5*i)
                tar.pendown()
                tar.pencolor(cor1)
                tar.begin_fill()
                quadrado()
                tar.color(cor1)
                tar.end_fill()
            elif matriz[i][j] == 2:
                tar.penup()
                tar.setpos(5 * j, -5 * i)
                tar.pendown()
                tar.pencolor(cor1)
                tar.begin_fill()
                quadrado()
                tar.color(cor2)
                tar.end_fill()
            elif matriz[i][j]==3:
                tar.penup()
                tar.setpos(5*j, -5*i)
                tar.pendown()
                tar.pencolor(cor1)
                tar.begin_fill()
                quadrado()
                tar.color(cor3)
                tar.end_fill()

#sistema
desenhar_Pixels(pixels1, '#ffffff', '#000000','#F80500', '#F7C192')
sleep(9)