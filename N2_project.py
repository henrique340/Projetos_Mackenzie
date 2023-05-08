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
def Cadastro_Candidatos():
   nome = input('Digite o nome do candidato: ')
   cargo = input('Digite o cargo do candidato: ').upper()
   while True:
      if cargo == 'GOVERNADOR:':
         lista_Candidatos_Governador.append(nome)
      elif cargo == 'PREFEITO':
         lista_Candidatos_Prefeito.append(nome)
      elif cargo == 'PRESIDENTE':
         lista_Candidatos_Presidente.append(nome)
      else:
         print('Insira um cargo válido: ')
Cadastro_Candidatos()