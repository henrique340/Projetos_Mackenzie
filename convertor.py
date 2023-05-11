# Funções

def bin_dec(binario):
    n = str(binario)
    decimal = 0
    exp = len(n)-1
    for i in range(len(n)):
        decimal += int(n[i])*2**exp
        exp -= 1
    return decimal

def bin_hex(binario):
def dec_hex(decimal):


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
