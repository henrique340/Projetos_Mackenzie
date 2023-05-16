#bibliotecas
from time import sleep
from operator import itemgetter

# Listas
lista_Candidatos_Governador = []
Partidos_Governador = []
lista_Voto_Governador = []
lista_Candidatos_Presidente = []
Partidos_Presidente = []
lista_Voto_Presidente = []
lista_Candidatos_Prefeito = []
Partidos_Prefeito = []
lista_Voto_Prefeito = []
lista_eleitores = []

#variáveis
Voto_Branco_Prefeito = 0
Voto_Nulo_Prefeito = 0
Votos_Validos_Prefeito = 0
Voto_Branco_Governador = 0
Voto_Nulo_Governador = 0
Votos_Validos_Governador = 0
Voto_Branco_Presidente = 0
Voto_Nulo_Presidente = 0
Votos_Validos_Presidentes = 0

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
                Partidos_Governador.append(partido)
                print(f'O candidato {nome} do numero {numero}, do partido {partido} e do cargo {cargo} foi adicionado com sucesso')
                break
            elif cargo == 'PREFEITO':
                lista_Candidatos_Prefeito.append(nome)
                numero = lista_Candidatos_Prefeito.index(nome)
                partido = input('Digite o partido do candidato: ').upper()
                Partidos_Prefeito.append(partido)
                print(f'O candidato {nome} do numero {numero}, do partido {partido} e do cargo {cargo} foi adicionado com sucesso')
                break
            elif cargo == 'PRESIDENTE':
                lista_Candidatos_Presidente.append(nome)
                numero = lista_Candidatos_Presidente.index(nome)
                partido = input('Digite o partido do candidato: ').upper()
                Partidos_Presidente.append(partido)
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
    global Votos_Validos_Prefeito
    global Voto_Branco_Governador
    global Voto_Nulo_Governador
    global Votos_Validos_Governador
    global Voto_Branco_Presidente
    global Voto_Nulo_Presidente
    global Votos_Validos_Presidente
    while True:
        nome = input('Digite o nome do eleitor: ').upper()
        if nome in lista_eleitores:

            # prefeito
            while True:
                print('-' * 45)
                print('Votação Prefeito')
                print('-' * 45)
                print('Para votar branco [vote -1]')
                print('Para votar nulo [vote -2]')
                for i, candidato in enumerate(lista_Candidatos_Prefeito):
                    print(f'{i} - {candidato} ({Partidos_Prefeito[i]})')
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
                    print(f'O número {voto_prefeito} é o candidato {lista_Candidatos_Prefeito[voto_prefeito]} do partido {Partidos_Prefeito[voto_prefeito]}')
                    confirmacao = input('Deseja confirmar o voto: [Sim]/Não] ').upper()
                    if confirmacao == 'SIM':
                        Votos_Validos_Prefeito += 1
                        lista_Voto_Prefeito = [(candidato, 0, '', '', 0) for candidato in lista_Candidatos_Prefeito]
                        for i in range(len(lista_Candidatos_Prefeito)):
                            if lista_Voto_Prefeito[i][0] == lista_Candidatos_Prefeito[voto_prefeito]:
                                lista_Voto_Prefeito[i] = (lista_Voto_Prefeito[i][0], i, Partidos_Prefeito[i], 'PREFEITO', lista_Voto_Prefeito[i][4]+1)
                    elif confirmacao == 'NAO':
                        print('Voto cancelado')
                    else:
                        print('opção inválida, tente novamente')

                    # governador
                    while True:
                        print('-' * 45)
                        print('Votação Governador')
                        print('-' * 45)
                        print('Para votar branco [vote -1]')
                        print('Para votar nulo [vote -2]')
                        for i, candidato in enumerate(lista_Candidatos_Governador):
                            print(f'{i} - {candidato} ({Partidos_Governador[i]})')
                        voto_governador = int(input('Digite seu voto: '))
                        if voto_governador == -1:
                            print(f'O eleitor {nome} votou em branco')
                            confirmacao = input('Deseja confirmar o voto: [Sim]/Não] ').upper()
                            Voto_Branco_Governador += 1
                        elif voto_governador == -2:
                            print(f'O eleitor {nome} votou nulo')
                            confirmacao = input('Deseja confirmar o voto: [Sim]/[Não] ').upper()
                            Voto_Nulo_Governador += 1
                        elif voto_governador >= 0:
                            print(f'O número {voto_governador} é o candidato {lista_Candidatos_Governador[voto_governador]} do partido {Partidos_Governador[voto_governador]}')
                            confirmacao = input('Deseja confirmar o voto: [Sim]/Não] ').upper()
                            if confirmacao == 'SIM':
                                Votos_Validos_Governador += 1
                                lista_Voto_Governador = [(candidato, 0, '', '', 0) for candidato in lista_Candidatos_Governador]
                                for i in range(len(lista_Candidatos_Governador)):
                                    if lista_Voto_Governador[i][0] == lista_Candidatos_Prefeito[voto_governador]:
                                        lista_Voto_Governador[i] = (lista_Voto_Governador[i][0], i, Partidos_Governador[i], 'GOVERNADOR',lista_Voto_Governador[i][4] + 1)
                            elif confirmacao == 'NAO':
                                print('Voto cancelado')
                            else:
                                print('opção inválida, tente novamente')

                            # presidente
                            while True:
                                print('-' * 45)
                                print('Votação Presidente')
                                print('-' * 45)
                                print('Para votar branco [vote -1]')
                                print('Para votar nulo [vote -2]')
                                for i, candidato in enumerate(lista_Candidatos_Presidente):
                                    print(f'{i} - {candidato} ({Partidos_Presidente[i]})')
                                voto_presidente = int(input('Digite seu voto: '))
                                if voto_presidente == -1:
                                    print(f'O eleitor {nome} votou em branco')
                                    confirmacao = input('Deseja confirmar o voto: [Sim]/Não] ').upper()
                                    Voto_Branco_Presidente += 1
                                elif voto_presidente == -2:
                                    print(f'O eleitor {nome} votou nulo')
                                    confirmacao = input('Deseja confirmar o voto: [Sim]/[Não] ').upper()
                                    Voto_Nulo_Presidente += 1
                                elif voto_presidente >= 0:
                                    print(f'O número {voto_presidente} é o candidato {lista_Candidatos_Presidente[voto_presidente]} do partido {Partidos_Presidente[voto_presidente]}')
                                    confirmacao = input('Deseja confirmar o voto: [Sim]/Não] ').upper()
                                    if confirmacao == 'SIM':
                                        Votos_Validos_Presidente += 1
                                        lista_Voto_Presidente = [(candidato, 0, '', '', 0) for candidato in lista_Candidatos_Presidente]
                                        for i in range(len(lista_Candidatos_Presidente)):
                                            if lista_Voto_Presidente[i][0] == lista_Candidatos_Presidente[voto_prefeito]:
                                                lista_Voto_Presidente[i] = (lista_Voto_Presidente[i][0], i, Partidos_Presidente[i],'PRESIDENTE', lista_Voto_Presidente[i][4] + 1)
                                                print('Voto sendo adicionado ...')
                                                sleep(3)
                                                print('-' * 45)
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
    # presidente
    print('-' * 66)
    print('|            RANKING DO RESULTADO PARA PRESIDENTE                |')
    print('-' * 66)
    print('|   Nome   |   Partido  |  Total de votos  |   % votos válidos   |')
    print('-' * 66)
    ranking_presidente = sorted(lista_Voto_Presidente, key=itemgetter(4), reverse=True)
    count = 1
    for count, (candidato, numero, partido, cargo, votos) in enumerate(ranking_presidente):
        print(f'{count} {candidato}|{partido}|{votos}|{100*votos/(Voto_Nulo_Presidente+Voto_Branco_Presidente+Votos_Validos_Presidentes)}')
    print('-'*66)
    print(f'| Total de votos = {Votos_Validos_Presidentes+Voto_Nulo_Presidente+Voto_Branco_Presidente}|')
    print(f'| Total de votos válidos = {Votos_Validos_Presidentes} e % {100*Votos_Validos_Presidentes/(Voto_Nulo_Presidente+Voto_Branco_Presidente+Votos_Validos_Presidentes)} |')
    print(f'| Total de votos brancos = {Voto_Branco_Presidente} e % {100*Voto_Branco_Presidente/(Voto_Nulo_Presidente+Voto_Branco_Presidente+Votos_Validos_Presidentes)} |')
    print(f'| Total de votos nulos = {Voto_Nulo_Presidente} e % {100*Voto_Nulo_Presidente/(Voto_Nulo_Presidente+Voto_Branco_Presidente+Votos_Validos_Presidentes)} |')

    # governador
    print('-' * 66)
    print('|            RANKING DO RESULTADO PARA GOVERNADOR                |')
    print('-' * 66)
    print('|   Nome   |   Partido  |  Total de votos  |   % votos válidos   |')
    print('-' * 66)
    ranking_governador = sorted(lista_Voto_Presidente, key=itemgetter(4), reverse=True)
    count = 1
    for count, (candidato, numero, partido, cargo, votos) in enumerate(ranking_governador):
        print(f'{count} {candidato}|{partido}|{votos}|{100 * votos / (Voto_Nulo_Governador + Voto_Branco_Governador + Votos_Validos_Governador)}')
    print('-' * 66)
    print(f'| Total de votos = {Votos_Validos_Governador + Voto_Nulo_Governador + Voto_Branco_Governador}|')
    print(f'| Total de votos válidos = {Votos_Validos_Governador} e % {100 * Votos_Validos_Governador / (Voto_Nulo_Governador + Voto_Branco_Governador + Votos_Validos_Governador)} |')
    print(f'| Total de votos brancos = {Voto_Branco_Governador} e % {100 * Voto_Branco_Governador / (Voto_Nulo_Governador + Voto_Branco_Governador + Votos_Validos_Governador)} |')
    print(f'| Total de votos nulos = {Voto_Nulo_Governador} e % {100 * Voto_Nulo_Governador/ (Voto_Nulo_Governador + Voto_Branco_Governador + Votos_Validos_Governador)} |')

    # prefeito
    print('-' * 66)
    print('|            RANKING DO RESULTADO PARA PREFEITO                  |')
    print('-' * 66)
    print('|   Nome   |   Partido  |  Total de votos  |   % votos válidos   |')
    print('-' * 66)
    ranking_prefeito = sorted(lista_Voto_Prefeito, key=itemgetter(4), reverse=True)
    count = 1
    for count, (candidato, numero, partido, cargo, votos) in enumerate(ranking_prefeito):
        print(f'{count} {candidato}|{partido}|{votos}|{100 * votos / (Voto_Nulo_Prefeito + Voto_Branco_Prefeito + Votos_Validos_Prefeito)}')
    print('-' * 66)
    print(f'| Total de votos = {Votos_Validos_Prefeito + Voto_Nulo_Prefeito + Voto_Branco_Prefeito}|')
    print(f'| Total de votos válidos = {Votos_Validos_Prefeito} e % {100 * Votos_Validos_Prefeito / (Voto_Nulo_Prefeito + Voto_Branco_Prefeito + Votos_Validos_Prefeito)} |')
    print(f'| Total de votos brancos = {Voto_Branco_Prefeito} e % {100 * Voto_Branco_Prefeito / (Voto_Nulo_Prefeito + Voto_Branco_Prefeito + Votos_Validos_Prefeito)} |')
    print(f'| Total de votos nulos = {Voto_Nulo_Prefeito} e % {100 * Voto_Nulo_Prefeito / (Voto_Nulo_Prefeito + Voto_Branco_Prefeito + Votos_Validos_Prefeito)} |')

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
    elif opc == 4:
        Resultado()
    elif opc == 6:
        print('Encerrando o programa')
        break