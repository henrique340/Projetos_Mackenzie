#bibliotecas
from time import sleep
from operator import itemgetter

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
                partido = input('Digite o partido do candidato: ').upper()
                lista_Partidos_Governador.append(partido)
                print(f'O candidato {nome} do numero {numero}, do partido {partido} e do cargo {cargo} foi adicionado com sucesso')
                break
            elif cargo == 'PREFEITO':
                lista_Candidatos_Prefeito.append(nome)
                numero = lista_Candidatos_Prefeito.index(nome)
                partido = input('Digite o partido do candidato: ').upper()
                lista_Partidos_Prefeito.append(partido)
                print(f'O candidato {nome} do numero {numero}, do partido {partido} e do cargo {cargo} foi adicionado com sucesso')
                break
            elif cargo == 'PRESIDENTE':
                lista_Candidatos_Presidente.append(nome)
                numero = lista_Candidatos_Presidente.index(nome)
                partido = input('Digite o partido do candidato: ').upper()
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
        if nome.isalpha():
            lista_eleitores.append(nome)
            while True:
                cpf = input('Digite o CPF do eleitor: ')
                if len(cpf) == 11:
                    lista_eleitores.append(cpf)
                    print(f'o eleitor {nome} de cpf {cpf} foi adicionado com sucesso')
                    break
                else:
                    print('Digite um numero de cpf válido')
            opc = input('Deseja cadastrar outro candidato? [Sim]/[Nao] ').upper()
            if opc == 'NAO':
                break
        else:
            print('Erro, tente novamente')

def Votar():
    global Voto_Branco_Prefeito
    global Voto_Nulo_Prefeito
    global Voto_Branco_Governador
    global Voto_Nulo_Governador
    global Voto_Branco_Presidente
    global Voto_Nulo_Presidente
    while True:
        nome = input('Digite o nome do eleitor: ').upper()
        if nome in lista_eleitores:

            # prefeito
            lista_Voto_Prefeito = [(candidato, 0) for candidato in lista_Candidatos_Prefeito]
            while True:
                print('-' * 45)
                print('Votação Prefeito')
                print('-' * 45)
                print('Para votar branco [vote -1]')
                print('Para votar nulo [vote -2]')
                for i, candidato in enumerate(lista_Candidatos_Prefeito):
                    print(f'{i} - {candidato} ({lista_Partidos_Prefeito[i]})')
                voto_prefeito = int(input('Digite seu voto: '))
                if voto_prefeito == -1:
                    print(f'O eleitor {nome} votou em branco')
                    confirmacao = input('Deseja confirmar o voto? [Sim]/Não] ').upper()
                    Voto_Branco_Prefeito += 1
                elif voto_prefeito == -2:
                    print(f'O eleitor {nome} votou nulo')
                    confirmacao = input('Deseja confirmar o voto? [Sim]/[Não] ').upper()
                    Voto_Nulo_Prefeito += 1
                elif voto_prefeito >= 0:
                    print(f'O número {voto_prefeito} é o candidato {lista_Candidatos_Prefeito[voto_prefeito]} do partido {lista_Partidos_Prefeito[voto_prefeito]}')
                    confirmacao = input('Deseja confirmar o voto: [Sim]/Não] ').upper()
                    if confirmacao == 'SIM':
                        for i in range(len(lista_Voto_Prefeito)):
                            if lista_Voto_Prefeito[i][0] == lista_Candidatos_Prefeito[voto_prefeito]:
                                lista_Voto_Prefeito[i] = (lista_Voto_Prefeito[i][0], lista_Voto_Prefeito[i][1] + 1)
                    elif confirmacao == 'NAO':
                        print('Voto cancelado')
                    else:
                        print('opção inválida, tente novamente')

                    # governador
                    lista_Voto_Governador = [(candidato, 0) for candidato in lista_Candidatos_Governador]
                    while True:
                        print('-' * 45)
                        print('Votação Governador')
                        print('-' * 45)
                        print('Para votar branco [vote -1]')
                        print('Para votar nulo [vote -2]')
                        for i, candidato in enumerate(lista_Candidatos_Governador):
                            print(f'{i} - {candidato} ({lista_Partidos_Governador[i]})')
                        voto_governador = int(input('Digite seu voto: '))
                        if voto_governador == -1:
                            print(f'O eleitor {nome} votou em branco')
                            confirmacao = input('Deseja confirmar o voto: [Sim]/Não] ').upper()
                            Voto_Branco_Governador += 1
                        elif voto_governador == -2:
                            print(f'O eleitor {nome} votou nulo')
                            confirmacao = input('Deseja confirmar o voto: [Sim]/[Não] ').upper()
                            Voto_Nulo_Governador += 1
                        elif voto_governador>=0:
                            print(f'O número {voto_governador} é o candidato {lista_Candidatos_Governador[voto_governador]} do partido {lista_Partidos_Governador[voto_governador]}')
                            confirmacao = input('Deseja confirmar o voto: [Sim]/Não] ').upper()
                            if confirmacao == 'SIM':
                                for i in range(len(lista_Voto_Governador)):
                                    if lista_Voto_Governador[i][0] == lista_Candidatos_Governador[voto_prefeito]:
                                        lista_Voto_Governador[i] = (lista_Voto_Governador[i][0], lista_Voto_Governador[i][1] + 1)
                            elif confirmacao == 'NAO':
                                print('Voto cancelado')
                            else:
                                print('opção inválida, tente novamente')

                            # presidente
                            lista_Voto_Presidente = [(candidato, 0) for candidato in lista_Candidatos_Presidente]
                            while True:
                                print('-' * 45)
                                print('Votação Presidente')
                                print('-' * 45)
                                print('Para votar branco [vote -1]')
                                print('Para votar nulo [vote -2]')
                                for i, candidato in enumerate(lista_Candidatos_Presidente):
                                    print(f'{i} - {candidato} ({lista_Partidos_Presidente[i]})')
                                voto_presidente = int(input('Digite seu voto: '))
                                if voto_presidente == -1:
                                    print(f'O eleitor {nome} votou em branco')
                                    confirmacao = input('Deseja confirmar o voto: [Sim]/Não] ').upper()
                                    Voto_Branco_Presidente[voto_presidente] += 1
                                elif voto_presidente == -2:
                                    print(f'O eleitor {nome} votou nulo')
                                    confirmacao = input('Deseja confirmar o voto: [Sim]/[Não] ').upper()
                                    Voto_Nulo_Presidente[voto_presidente] += 1
                                elif voto_presidente>=0:
                                    print(f'O número {voto_presidente} é o candidato {lista_Candidatos_Presidente[voto_presidente]} do partido {lista_Partidos_Presidente[voto_presidente]}')
                                    confirmacao = input('Deseja confirmar o voto: [Sim]/Não] ').upper()
                                    if confirmacao == 'SIM':
                                        for i in range(len(lista_Voto_Presidente)):
                                            if lista_Voto_Presidente[i][0] == lista_Candidatos_Presidente[voto_presidente]:
                                                lista_Voto_Presidente[i] = (lista_Voto_Presidente[i][0], lista_Voto_Presidente[i][1] + 1)
                                                print('Voto sendo adicionado ...')
                                                sleep(3)
                                                print('-'*45)
                                        break
                                    elif confirmacao == 'NAO':
                                        print('Voto cancelado')
                                    else:
                                        print('opção inválida, tente novamente')
                                else:
                                    print('Erro, digite um voto válido')

                        else:
                            print('erro, digite um voto válido')

                else:
                    print('erro, digite um voto válido')

        else:
            print('Erro, o eleitor não foi cadastrado')
        break


def Resultado():
    #presidente
    print('-' * 66)
    print('|            RANKING DO RESULTADO PARA PRESIDENTE                |')
    print('-' * 66)
    print('|   Nome   |   Partido  |  Total de votos  |   % votos válidos   |')
    print('-' * 66)
    ranking_presidente = sorted(lista_Voto_Presidente, key=itemgetter(1), reverse=True)
    count = 1
    for count, (candidato, votos) in enumerate(ranking_presidente):
        print(f'{count} {candidato}| |{votos}|')

    #governador
    ranking_governador = sorted(lista_Voto_Governador, key=itemgetter(1), reverse=True)
    print('-' * 66)
    print('|            RANKING DO RESULTADO PARA GOVERNADOR                |')
    print('-' * 66)
    print('|   Nome   |   Partido  |  Total de votos  |   % votos válidos   |')
    print('-' * 66)
    count = 1
    for count, (candidato, votos) in enumerate(ranking_governador):
        print(f'{count} {candidato}| |{votos}|')

    #prefeito
    ranking_prefeito = sorted(lista_Voto_Prefeito, key=itemgetter(1), reverse=True)
    print('-' * 66)
    print('|            RANKING DO RESULTADO PARA PREFEITO                  |')
    print('-' * 66)
    print('|   Nome   |   Partido  |  Total de votos  |   % votos válidos   |')
    print('-' * 66)
    count = 1
    for count, (candidato, votos) in enumerate(ranking_prefeito):
        print(f'{count} {candidato}| |{votos}|')

# sistema
while True:
    Menu()
    opc = int(input('Digite sua escolha: '))
    if opc == 1:
        Cadastro_Candidatos()
    elif opc == 2:
        Cadastrar_Eleitores()
    elif opc == 3:
        Votar()
    elif opc == 6:
        print('Encerrando o programa')
        break