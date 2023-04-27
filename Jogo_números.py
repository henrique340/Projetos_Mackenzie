# jogo do tiktok que precisa sortear
# 4 números diferentes de 0 a 9 para
# descobrir quais são eles e a sequência correta
from random import randint
lista = []


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
print(lista)

# usuário escolhendo

list = []
while list != lista:
    list = []
    m1, m2, m3, m4 = input('Digite 4 números: ').split(' ')
    list.append(m1)
    list.append(m2)
    list.append(m3)
    list.append(m4)
    print(list)

    pos = 0
    count = 0
    for c in range(0, 3):
        if list[c] == list[c]:
            count += 1
        else:
            while list[c] != lista[c]:



