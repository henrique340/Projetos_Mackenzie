from random import randint
matriz = []
for i in range(4):
    print('[0]'*4)
while True:
    print(matriz)

    #apresentação dos comandos
    print('''os comandos são os seguintes:
    W ou w: cima
    S ou s: baixo
    D ou d: direita
    A ou a: esquerda''')

    linha = randint(0, 3)
    coluna = randint(0, 3)
    while matriz[linha][coluna] != 0:
        linha = randint(0, 3)
        coluna = randint(0, 3)
    matriz[linha][coluna] = 2

    print(matriz)
