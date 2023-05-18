# 1 juntando duas listas em um dicionário
import locale

key_lista = ['A', 'B', 'C']
valor_lista = ['azul', 'vermelho', 'preto']

print(1)
dic_1 = dict(zip(key_lista, valor_lista))
print(dic_1)

dic_2 = {key:valor for key, valor in zip(key_lista, valor_lista)}
print(dic_2)

itens = zip(key_lista, valor_lista)
dict_3 = {}
for key , valor in itens:
    if key in dict_3:
        pass #para evitar repetir keys
    else:
        dict_3[key] = valor

print(dict_3)


# 2 juntar duas ou mais listas em uma lista de listas
print(2)

def juntar(*args, valor_falta = None):
    comprimento_max = max([len(lst) for lst in args])
    outlist = []
    for i in range(comprimento_max):
        outlist.append([args[k][i] if i < len(args[k]) else valor_falta for k in range(len(args))])
    return outlist
print(juntar([1, 2, 3], [4, 5, 6], ['a', 'b', 'c']))


# 3 ordenar uma lista de dicionários
print(3)
dicts_lista = [ {'nome': 'james', 'idade': 13} , {'nome': 'may', 'idade': 23}, {'nome': 'aty', 'idade': 14} ]


dicts_lista.sort(key=lambda item: item.get('idade'))
print(dicts_lista)

from operator import itemgetter
f = itemgetter('nome')
dicts_lista.sort(key=f)
print(dicts_lista)


# 4 ordenar uma lista de strings
print(4)
minha_lista = ['azul', 'verde', 'vermelho']

minha_lista.sort()
minha_lista = sorted(minha_lista, key=len, reverse = False)
print(minha_lista)

import locale
from functools import cmp_to_key
minha_lista = sorted(minha_lista, key=cmp_to_key(locale.strcoll), reverse=False)
print(minha_lista)


# 5 ordenar uma lista baseada em outra lista
print(5)
a = ['azul', 'verde', 'laranja', 'roxo', 'amarelo']
b = [3, 2, 5, 4, 1]

sortedLista = [val for (_, val) in sorted(zip(b, a), key=lambda x: x[0])]
print(sortedLista)


# 6 Mapear uma lista em um dicionário
print(6)
minhalista = ['azul', 'laranja', 'verde']

