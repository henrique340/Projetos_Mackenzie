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

    # gera aleatoriamente o número 2 em uma posição
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

    # ganhar
    for i in range(4):
        for j in range(4):
            if matriz[i][j]==2048:
                return 'Você ganhou'

    # Se tiver 0 no jogo, ele continua
    for i in range(4):
        for j in range(4):
            if matriz[i][j]==0:
                return 'Jogo continua'

    # se tiver dois números iguais lado a lado, ele continua
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == matriz[i+1][j] or matriz[i][j] == matriz[i][j+1]:
                return 'Jogo continua'

    # Se tiver números iguais na mesma linha, o jogo continua
    for j in range(3):
        if matriz[3][j] == matriz[3][j+1]:
            return 'Jogo continua'

    # Se tiver números iguais na mesma coluna, o jogo continua
    for i in range(3):
        if matriz[i][3] == matriz[i+1][3]:
            return 'Jogo continua'
    # perde
    return 'Você perdeu'



# Função para comprimir
def comprimir(matriz):
    trocar = False
    nova_matriz = []
    for i in range(4):
        nova_matriz.append([0]*4)    # cria uma nova matriz 4x4

    for i in range(4):
        pos = 0
        for j in range(4):
            if (matriz[i][j] != 0):
                nova_matriz[i][pos] = matriz[i][j]
                if (j != pos):
                    trocar = True
                    pos += 1
    return nova_matriz, trocar

#função para juntar
def juntar(matriz):
    trocar = False

    for i in range(4):
        for j in range(3):
            if (matriz[i][j] == matriz[i][j+1] and matriz[i][j] != 0):
                matriz[i][j] = matriz[i][j]*2
                matriz[i][j+1] = 0
                trocar = True
    return matriz, trocar


#função para reverter
def reverso(matriz):
    nova_matriz = []
    for i in range(4):
        nova_matriz.append([])
        for j in range(4):
            nova_matriz[1].append(matriz[i][3-j])
    return nova_matriz


#função transposição
def transposicao(matriz):
    nova_matriz = []
    for i in range(4):
        nova_matriz.append([])
        for j in range(4):
            nova_matriz[i].append(matriz[j][i])
    return nova_matriz


def mover_esquerda(grid):

    novo_grid, trocar1 = comprimir(grid)

    novo_grid, trocar2 = juntar(novo_grid)

    trocar = trocar1 or trocar2

    novo_grid, temp = comprimir(novo_grid)

    return novo_grid, temp

def mover_direita(grid):

    novo_grid = reverso(grid)

    novo_grid, trocar = mover_esquerda(novo_grid)

    novo_grid = reverso(novo_grid)

    return novo_grid, trocar


def mover_cima(grid):

    novo_grid = transposicao(grid)

    novo_grid, trocar = mover_esquerda(novo_grid)

    novo_grid = transposicao(novo_grid)

    return novo_grid, trocar


def mover_baixo(grid):

    novo_grid = transposicao(grid)

    novo_grid, trocar = mover_direita(novo_grid)

    novo_grid = transposicao(novo_grid)

    return novo_grid, trocar


#sistema
inicio_do_jogo()
