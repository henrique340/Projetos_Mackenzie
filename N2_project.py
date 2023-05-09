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
            while True:
                print('-' * 45)
                print('Votação Prefeito')
                print('-' * 45)
                print('Para votar branco [vote -1]')
                print('Para votar nulo [vote -2]')
                voto = input('Digite seu voto: ')
                if voto == '-1':
                    print(f'O eleitor {nome} votou em branco')
                    confirmacao = input('Deseja confirmar o voto? [Sim]/Não] ').upper()
                    Voto_Branco_Prefeito += 1
                elif voto == '-2':
                    print(f'O eleitor {nome} votou nulo')
                    confirmacao = input('Deseja confirmar o voto? [Sim]/[Não] ').upper()
                    Voto_Nulo_Prefeito += 1
                elif voto.isdigit():
                    print(f'O número {voto} é o candidato {lista_Candidatos_Prefeito[int(voto)]} do partido {lista_Partidos_Prefeito[int(voto)]}')
                    confirmacao = input('Deseja confirmar o voto: [Sim]/Não] ').upper()
                    if confirmacao == 'SIM':
                        a = lista_Candidatos_Prefeito[int(voto)][int(voto)]
                        a += 1
                    else:
                        print('Cancelando voto ...')

            # governador
            while True:
                print('-' * 45)
                print('Votação Governador')
                print('-' * 45)
                print('Para votar branco [vote -1]')
                print('Para votar nulo [vote -2]')
                voto = input('Digite seu voto: ')
                if voto == '-1':
                    print(f'O eleitor {nome} votou em branco')
                    confirmacao = input('Deseja confirmar o voto: [Sim]/Não] ').upper()
                    Voto_Branco_Governador += 1
                elif voto == '-2':
                    print(f'O eleitor {nome} votou nulo')
                    confirmacao = input('Deseja confirmar o voto: [Sim]/[Não] ').upper()
                    Voto_Nulo_Governador += 1
                elif voto.isdigit():
                    print(
                        f'O número {voto} é o candidato {lista_Candidatos_Governador[int(voto)]} do partido {lista_Partidos_Governador[int(voto)]}')
                    confirmacao = input('Deseja confirmar o voto: [Sim]/Não] ').upper()
                    if confirmacao == 'SIM':
                        a = lista_Candidatos_Governador[int(voto)][int(voto)]
                        a += 1
                    else:
                        print('Cancelando voto ...')
                        break

            # presidente
            while True:
                print('-' * 45)
                print('Votação Presidente')
                print('-' * 45)
                print('Para votar branco [vote -1]')
                print('Para votar nulo [vote -2]')
                voto = input('Digite seu voto: ')
                if voto == '-1':
                    print(f'O eleitor {nome} votou em branco')
                    confirmacao = input('Deseja confirmar o voto: [Sim]/Não] ').upper()
                    Voto_Branco_Presidente[voto] += 1
                elif voto == '-2':
                    print(f'O eleitor {nome} votou nulo')
                    confirmacao = input('Deseja confirmar o voto: [Sim]/[Não] ').upper()
                    Voto_Nulo_Presidente[voto] += 1
                elif voto.isdigit():
                    print(
                        f'O número {voto} é o candidato {lista_Candidatos_Presidente[int(voto)]} do partido {lista_Partidos_Presidente[int(voto)]}')
                    confirmacao = input('Deseja confirmar o voto: [Sim]/Não] ').upper()
                    if confirmacao == 'SIM':
                        a = int(lista_Candidatos_Presidente[int(voto)][int(voto)])
                        a += 1
                    else:
                        print('Cancelando voto ...')
                        break
                break
        else:
            print('Erro, tente novamente')
            continue


def Resultado():
    print('-' * 66)
    print('|            RANKING DO RESULTADO PARA PRESIDENTE                |')
    print('-' * 66)
    print('|   Nome   |   Partido  |  Total de votos  |   % votos válidos   |')
    print('-' * 66)
    posicao = max(lista_Candidatos_Presidente).index()
    print(lista_Candidatos_Presidente[posicao])


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
