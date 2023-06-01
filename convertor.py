# Funções
def bin_dec(binario):
    n = str(binario)
    decimal = 0
    exp = len(n)-1
    for i in range(len(n)):
        decimal += int(n[i])*2**exp
        exp -= 1
    return decimal

def bin_hex(bin):
    dec = bin_dec(bin)
    return dec_hex(dec)

def dec_bin(decimal):
    binario = []
    while decimal > 0:
        resto = decimal % 2
        binario.insert(0, str(resto))
        decimal //= 2
    return ''.join(binario)


def dec_hex(decimal):
    tabela_conversao = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
    hexadecimal = []
    while decimal > 0:
        hexadecimal.append(tabela_conversao[(decimal % 16)])
        decimal = decimal // 16
    for item in range(len(hexadecimal)-1, -1, -1):
        print(hexadecimal[item], end='')


def hexa_dec(hexadecimal):
    tabela_conversao = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                        5: '5', 6: '6', 7: '7',
                        8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c',
                        13: 'd', 14: 'e', 15: 'f'}
    n = str(hexadecimal)
    exp = len(n)-1
    decimal = 0
    for i in range(len(n)):
        if n[i].lower() in tabela_conversao.values():
            valor_decimal = list(tabela_conversao.keys())[list(tabela_conversao.values()).index(n[i].lower())]
            decimal += valor_decimal * (16 ** exp)
        else:
            return "O número hexadecimal é inválido."
        exp -= 1
    return decimal


#sistema
while True:
    print('''Opções
    Binario
    Decimal
    Hexadecimal
    Sair''')
    base = input('Quer converter de: ').upper()
    if base == 'SAIR':
        break
    conversao = input('Para: ').upper()
    if base == 'BINARIO' and conversao == 'DECIMAL':
        bin = int(input('Digite o número em binário: '))
        print(f'o decimal de {bin} é {bin_dec(bin)}')
    elif base == 'BINARIO' and conversao == 'HEXADECIMAL':
        bin = int(input('Digite o número em binário: '))
        print(f'o hexadecimal de {bin} é ', end='')
        bin_hex(bin)
        print('\n')
    elif base == 'DECIMAL' and conversao == 'BINARIO':
        dec = int(input('Digite o número em decimal: '))
        print(f'o binário de {dec} é {dec_bin(dec)}')
    elif base == 'DECIMAL' and conversao == 'HEXADECIMAL':
        dec = int(input('Digite o número em decimal: '))
        print(f'o hexadecimal de {dec} é ',end='')
        dec_hex(dec)
        print('\n')
    elif base == 'HEXADECIMAL' and conversao == 'BINARIO':
        hex = input('Digite o número em hexadecimal: ')
        print(f'o binário de {hex} é {dec_bin(hexa_dec(hex))}')
    elif base == 'HEXADECIMAL' and conversao == 'DECIMAL':
        hex = input('Digite o número em hexadecimal: ')
        print(f'o decimal de {hex} é {hexa_dec(hex)}')
    else:
        print('Erro, tente novamente')