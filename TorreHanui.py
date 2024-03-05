# funções

def TrocarPosicao(disco, pilha):
    if disco in Pilha1:
        Pilha1.pop()
        if pilha == 2:
            Pilha2.append(disco)
        elif pilha == 3:
            Pilha3.append(disco)
    elif disco in Pilha2:
        Pilha2.pop()
        if pilha == 1:
            Pilha1.append(disco)
        elif pilha == 3:
            Pilha3.append(disco)
    elif disco in Pilha3:
        Pilha3.pop()
        if pilha == 1:
            Pilha1.append(disco)
        elif pilha == 2:
            Pilha2.append(disco)


def Situacao(pilha1, pilha2, pilha3):
    print(f'Pilha 1: {Pilha1}')
    print(f'Pilha 2: {Pilha2}')
    print(f'Pilha 3: {Pilha3}')

# sistema

print('''\nTorre de Hanui\n
O jogo consiste em empilhar corretamente os discos 
Regra 1: só pode mover um disco por vez
Regra 2: um disco só pode ser colocado em um espaço vazio ou em cima de outro maior
Regra 3: os discos são nomeados pelo diametro de 1 a 6
Regra 4: as pilhas variam de 1 a 3
Regra 5: só é possível trocar um disco se ele estiver na última posição
--------------------------------------------------------------------------------------\n''')

Pilha1 = [6, 5, 4, 3, 2, 1]
Pilha2 = []
Pilha3 = []

while True:
    Situacao(Pilha1, Pilha2, Pilha3)
    disco, pilha = input('Digite o disco e a pilha no formato [num num]: ').split(' ')
    disco = int(disco)
    pilha = int(pilha)
    TrocarPosicao(disco, pilha)
