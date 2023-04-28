from random import randint
def inicio_do_jogo():

    #criar a matriz inicial

    matriz = []
    for i in range(4):
        matriz.append([0]*4)

    #apresentação dos comandos

    print('''os comandos são os seguintes:
    W ou w: cima
    S ou s: baixo
    D ou d: direita
    A ou a: esquerda''')

    gerar_2(matriz)
    return matriz

#Função para gerar o 2 em algum lugar da matriz

def gerar_2(matriz):
    linha = randint(0, 3)
    coluna = randint(0, 3)

    while matriz[linha][coluna] != 0:
        linha = randint(0, 3)
        coluna = randint(0, 3)

    matriz[linha][coluna] = 2


# Verificar as situações do jogo

def situacao(matriz):
    for i in range(4):
        for j in range(4):
            if matriz[i][j]==2048:
                return 'Você ganhou'

    for i in range(4):
        for j in range(4):
            if matriz[i][j]==0:
                return 'Jogo continua'

    for i in range(3):
        for j in range(3):
            if matriz[i][j] == matriz[i+1][j] or matriz[i][j] == matriz[i][j+1]:
                return 'Jogo continua'

    for j in range(3):
        if matriz[3][j] == matriz[3][j+1]:
            return 'Jogo continua'

    for i in range(3):
        if matriz[i][3] == matriz[i+1][3]:
            return 'Jogo continua'

    return 'Você perdeu'



# Função para juntar

def comprimir(matriz):
    