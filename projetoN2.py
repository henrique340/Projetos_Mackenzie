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


lista_Voto_Prefeito.append([0]*len(lista_Candidatos_Prefeito))
lista_Voto_Governador.append([0]*len(lista_Candidatos_Governador))
lista_Voto_Presidente.append([0]*len(lista_Candidatos_Presidente))

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
                voto_prefeito = int(input('Digite seu voto: '))
                if voto_prefeito == -1:
                    print(f'O eleitor {nome} votou em branco')
                    confirmacao = input('Deseja confirmar o voto? [Sim]/Não] ').upper()
                    Voto_Branco_Prefeito += 1
                elif voto_prefeito == -2:
                    print(f'O eleitor {nome} votou nulo')
                    confirmacao = input('Deseja confirmar o voto? [Sim]/[Não] ').upper()
                    Voto_Nulo_Prefeito += 1
                elif voto_prefeito>=0:
                    print(f'O número {voto_prefeito} é o candidato {lista_Candidatos_Prefeito[voto_prefeito]} do partido {lista_Partidos_Prefeito[voto_prefeito]}')
                    confirmacao = input('Deseja confirmar o voto: [Sim]/Não] ').upper()
                    if confirmacao == 'SIM':
                        lista_Voto_Prefeito[voto_prefeito] += 1

                        # governador
                        while True:
                            print('-' * 45)
                            print('Votação Governador')
                            print('-' * 45)
                            print('Para votar branco [vote -1]')
                            print('Para votar nulo [vote -2]')
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
                                    lista_Voto_Governador[voto_governador] += 1

                                    # presidente
                                    while True:
                                        print('-' * 45)
                                        print('Votação Presidente')
                                        print('-' * 45)
                                        print('Para votar branco [vote -1]')
                                        print('Para votar nulo [vote -2]')
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
                                                lista_Voto_Presidente[voto_presidente] += 1
                                                break
                                            else:
                                                print('Cancelando voto, tente novamente')
                                                continue
                                        else:
                                            print('Voto inválido, tente novamente')
                                            continue
                                else:
                                    print('Cancelando voto, tente novamente')
                                    continue
                            else:
                                print('Voto inválido, tente novamente')
                                continue
                    else:
                        print('Cancelando voto, tente novamente')
                        continue
                else:
                    print('Voto inválido, tente novamente')
                    continue
        else:
            print('Nome inválido, tente novamente')
            continue

