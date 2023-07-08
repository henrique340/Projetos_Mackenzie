print('-'*60)
print(f"{'SUPERMARKET PRICING':^60}")
print('-'*60)
print(f"{'|':<}{'Produtos': ^59}{'|':>}")
print(f"|\tbatata - R$8,91{'|':>42}")
print(f"|\tfrango - R$18,89{'|':>41}")
print(f"|\tpão - R$8,09{'|':>45}")
print(f"|\tsorvete - R$53,99{'|':>40}")
print('-'*60)


b = int(input('Deseja comprar quantas batatas? '))
f = int(input('Deseja comprar quantos frangos? '))
p = int(input('Deseja comprar quantos pães? '))
s = int(input('Deseja comprar quantos sorvetes? '))
batata = 8.91 * b
frango = 18.89 * f
pao = 8.09 * p
sorvete = 53.99 * s
print(f'Preço das batatas: R${batata:0.2f}')
print(f'Preço dos frangos: R${frango:0.2f}')
print(f'Preço dos pães: R${pao:0.2f}')
print(f'Preço dos sorvetes: R${sorvete:0.2f}')
print(f'Preço total: R${batata+frango+pao+sorvete:0.2f}')