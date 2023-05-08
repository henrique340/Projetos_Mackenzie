#Funções

def Menu():
   print('''1. Cadastrar candidatos
   2. Cadastrar eleitores 
   3. Votar
   4. Apurar resultados
   5. Relatório estatísticas 
   6. Encerrar ''')
lista_Candidatos_Governador = []
lista_Candidatos_Presidente = []
lista_Candidatos_Prefeito = []
lista_eleitores = []
def Cadastro_Candidatos():
   while True:
      nome = input('Digite o nome do candidato: ')
      partido = input('Digite o partido do candidato: ')
      while True:
         cargo = input('Digite o cargo do candidato: ').upper()
         if cargo == 'GOVERNADOR:':
            lista_Candidatos_Governador.append(nome)
            numero = 3 * str(lista_Candidatos_Governador.index(nome))
            print(f'O candidato {nome} do numero {numero}, do partido {partido} e do cargo {cargo} foi adicionado com sucesso')
            break
         elif cargo == 'PREFEITO':
            lista_Candidatos_Prefeito.append(nome)
            numero = 2*str(lista_Candidatos_Prefeito.index(nome))
            print(f'O candidato {nome} do numero {numero}, do partido {partido} e do cargo {cargo} foi adicionado com sucesso')
            break
         elif cargo == 'PRESIDENTE':
            lista_Candidatos_Presidente.append(nome)
            numero = 1 * str(lista_Candidatos_Presidente.index(nome))
            print(f'O candidato {nome} do numero {numero}, do partido {partido} e do cargo {cargo} foi adicionado com sucesso')
            break
         else:
            print('Insira um cargo válido: ')
      opc = input('Deseja cadastrar outro candidato? [Sim]/[Nao] ').upper()
      if opc == 'NAO':
          break
def Cadastrar_Eleitores():
   while True:
      nome = input('Digite o nome do eleitor: ')
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


#sistema
while True:
   Menu()
   opc = int(input('Digite sua escolha: '))
   if opc == 1:
      Cadastro_Candidatos()
   elif opc == 2:
      Cadastrar_Eleitores()
   elif opc == 6:
      print('Encerrando o programa')
      break