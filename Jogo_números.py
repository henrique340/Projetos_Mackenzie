# jogo do tiktok que precisa sortear
# 4 números diferentes de 0 a 9 para
# descobrir quais são eles e a sequência correta
from random import randint
lista = []
tentativas = 0


n1 = randint(0, 9)
lista.append(n1)


n2 = randint(0, 9)
while lista[0] == n2:
    n2 = randint(0, 9)
lista.append(n2)


n3 = randint(0, 9)
while lista[0] == n3 or lista[1] == n3:
    n3 = randint(0, 9)
lista.append(n3)


n4 = randint(0, 9)
while lista[0] == n4 or lista[1] == n4 or lista[2] == n4:
    n4 = randint(0, 9)
lista.append(n4)


# usuário escolhendo

list = []
while list != lista:
    list = []
    m1, m2, m3, m4 = input('Digite 4 números: ').split(' ')
    list.append(int(m1))
    list.append(int(m2))
    list.append(int(m3))
    list.append(int(m4))

    pos = 0
    count = 0
    for c in range(0, 4):
        if list[c] == lista[c]:
            pos += 1
        if list[c] in lista:
            count += 1

    # resultados da tentativa

    print(f'{list} - - você acertou {count} números - você acertou {pos} posições')
    tentativas += 1

print(f'você resolveu em {tentativas} tentativas')