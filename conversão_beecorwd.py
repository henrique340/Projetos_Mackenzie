tabela_conversao = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c',
                    13: 'd', 14: 'e', 15: 'f'}
def dec_hex(decimal):
    hexadecimal = ''
    while (decimal > 0):
        resto = decimal % 16
        hexadecimal = tabela_conversao[resto] + hexadecimal
        decimal = decimal // 16
    return hexadecimal
count =1
N=int(input(''))
for i in range(N):
    num, base = input('').split(' ')
    print(f'Case {i+1}:')
    if base == 'dec':
        binario = bin(int(num))
        bina = binario[2:]
        print(f'{dec_hex(int(num))} hex')
        print(f'{bina} bin')
    elif base == 'bin':
        x = int(num, 2)
        print(f'{x} dec')
        print(f'{dec_hex(x)} hex')
    elif base == 'hex':
        z = int(num, 16)
        binario = bin(z)
        bina = binario[2:]
        print(f'{z} dec')
        print(f'{bina} bin')
    i+=1
    print()