# Listas
lista_Candidatos_Governador = []
lista_Partidos_Governador = []
lista_Voto_Governador = []

lista_Candidatos_Presidente = []
lista_Partidos_Presidente = []
lista_Voto_Presidente = []

lista_Candidatos_Prefeito = []
lista_Partidos_Prefeito = []
lista_Voto_Prefeito = []

lista_eleitores = []

# Variáveis globais
Voto_Branco_Prefeito = 0
Voto_Nulo_Prefeito = 0
Voto_Branco_Governador = 0
Voto_Nulo_Governador = 0
Voto_Branco_Presidente = 0
Voto_Nulo_Presidente = 0


# Funções
def Menu():
    print('''1. Cadastrar candidatos
   2. Cadastrar eleitores 
   3. Votar
   4. Apurar resultados
   5. Relatório estatísticas 
   6. Encerrar ''')


def Cadastro_Candidatos():
    while True:
        nome = input('Digite o nome do candidato: ').upper()
        while True:
            cargo = input('Digite o cargo do candidato: ').upper()
            if cargo == 'GOVERNADOR':
                lista_Candidatos_Governador.append(nome)
                numero = lista_Candidatos_Governador.index(nome)
                partido = input('Digite o partido do candidato: ')
                lista_Partidos_Governador.append(partido)
                print(
                    f'O candidato {nome} do numero {numero}, do partido {partido} e do cargo {cargo} foi adicionado com sucesso')
                break
            elif cargo == 'PREFEITO':
                lista_Candidatos_Prefeito.append(nome)
                numero = lista_Candidatos_Prefeito.index(nome)
                partido = input('Digite o partido do candidato: ')
                lista_Partidos_Prefeito.append(partido)
                print(
                    f'O candidato {nome} do numero {numero}, do partido {partido} e do cargo {cargo} foi adicionado com sucesso')
                break
            elif cargo == 'PRESIDENTE':
                lista_Candidatos_Presidente.append(nome)
                numero = lista_Candidatos_Presidente.index(nome)
                partido = input('Digite o partido do candidato: ')
                lista_Partidos_Presidente.append(partido)
                print(
                    f'O candidato {nome} do numero {numero}, do partido {partido} e do cargo {cargo} foi adicionado com sucesso')
                break
            else:
                print('Insira um cargo válido: ')
        opc = input('Deseja cadastrar outro candidato? [Sim]/[Nao] ').upper()
        if opc == 'NAO':
            break


def Cadastrar_Eleitores():
    while True:
        nome = input('Digite o nome do eleitor: ').upper()
        lista_eleitores.append(nome)
        while True:
            cpf = input
# governador
print('Resultado da Eleição para Governador')
print('-' * 45)
for i, candidato in enumerate(lista_Candidatos_Governador):
    print(f'{candidato} ({lista_Partidos_Governador[i]}): {lista_Voto_Governador[i]} votos')
print(f'Votos brancos: {Voto_Branco_Governador}')
print(f'Votos nulos: {Voto_Nulo_Governador}')
print('-' * 45)

# presidente
print('Resultado da Eleição para Presidente')
print('-' * 45)
for i, candidato in enumerate(lista_Candidatos_Presidente):
    print(f'{candidato} ({lista_Partidos_Presidente[i]}): {lista_Voto_Presidente[i]} votos')
print(f'Votos brancos: {Voto_Branco_Presidente}')
print(f'Votos nulos: {Voto_Nulo_Presidente}')
print('-' * 45)
