tentativasTotais = 0
tentativasValidas = 0

#Funções
def TrocarPosicao(disco, pilha):
    global tentativasTotais, tentativasValidas
    if disco in Pilha1:
        if disco != Pilha1[-1]:
            print('Você só pode escolher o último disco')
            return
        tentativasValidas += 1
        if pilha == 2:
            if Pilha2 and Pilha2[-1] < disco:
                print('Não pode colocar um disco maior em um menor')
            else:
                Pilha1.pop()
                Pilha2.append(disco)
        elif pilha == 3:
            if Pilha3 and Pilha3[-1] < disco:
                print('Não pode colocar um disco maior em um menor')
            else:
                Pilha1.pop()
                Pilha3.append(disco)
        elif pilha == 1:
            pass
        else:
            print('Digite um valor válido')
    elif disco in Pilha2:
        if disco != Pilha2[-1]:
            print('Você só pode escolher o último disco')
            return
        tentativasValidas += 1
        if pilha == 1:
            if Pilha1 and Pilha1[-1] < disco:
                print('Não pode colocar um disco maior em um menor')
            else:
                Pilha2.pop()
                Pilha1.append(disco)
        elif pilha == 3:
            if Pilha3 and Pilha3[-1] < disco:
                print('Não pode colocar um disco maior em um menor')
            else:
                Pilha2.pop()
                Pilha3.append(disco)
        elif pilha == 2:
            pass
        else:
            print('Digite um valor valido')
    elif disco in Pilha3:
        if disco != Pilha3[-1]:
            print('Você só pode escolher o último disco')
            return
        tentativasValidas += 1
        if pilha == 1:
            if Pilha1 and Pilha1[-1] < disco:
                print('Não pode colocar um disco maior em um menor')
            else:
                Pilha3.pop()
                Pilha1.append(disco)
        elif pilha == 2:
            if Pilha2 and Pilha2[-1] < disco:
                print('Não pode colocar um disco maior em um menor')
            else:
                Pilha3.pop()
                Pilha2.append(disco)
        elif pilha == 3:
            pass
        else:
            print('Digite um valor valido')
    else:
        print('Digite um valor válido')


def Situacao(pilha1, pilha2, pilha3):
    print(f'Pilha 1: {Pilha1}')
    print(f'Pilha 2: {Pilha2}')
    print(f'Pilha 3: {Pilha3}')

#Sistema
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
    tentativasTotais += 1
    if Pilha2 == [6, 5, 4, 3, 2, 1] or Pilha3 == [6, 5, 4, 3 ,2, 1]:
        print('Parabens! Você ganhou o jogo')
        print(f'Tentativas totais: {tentativasTotais}')
        print(f'Tentativas válidas: {tentativasValidas}')
        break