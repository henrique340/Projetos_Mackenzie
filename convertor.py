# Funções
def base_dec(numero, base):
    resultado=[]
    n = str(numero)
    a = 0
    exp = len(n)-1
    for i in range(0, len(n)-1):
        a += n[i]*base**exp
        exp -= 1
    resultado.append(a)
    print(resultado)



# sistema

base_dec(101, 2)