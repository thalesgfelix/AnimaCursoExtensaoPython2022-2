# Primeiro projeto Python

#Sistema de votos
"""import os

votos_Lula = 0
votos_Bolsonaro = 0

while True:
  print('='*21)
  print('Total Lula:',votos_Lula)
  print('Total Bolsonaro:',votos_Bolsonaro)
  print('='*21)

  voto = int(input("Para quem gostaria de votar?\n13 - Lula\n22 - Bolsonaro\nSeu voto: "))
  try:
    if voto == 13:
      votos_Lula += 1
    elif voto == 22:
      votos_Bolsonaro += 1
    else: 
      pass

  except:
    print("Digite apenas 1 ou 2")
  
  os.system('clear')"""

#Aula 2

'''nome = input("Informe seu nome: ")
print(f"Boa noite, seu nome é {nome}")

idade = int(input("Qual a sua idade? "))
print(f"A sua idade é  {idade} ano(s)")

dobIdade = idade * 2
print("O dobro da sua idade é: ", dobIdade)

#Estrutura condicional - o famoso "SE" (if)
#Se a pessoa for maior de idade, mostre "Você é maior de idade, ótimo! Já pode beber ou dirigir"
if idade >= 18:
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir")

else :
  print("Você é jovem ainda, jovem ainda...")

genero = input("Informe o gênero M = Masculino, F = Feminino: ")
if idade >= 18 and genero == "M":
  print ("... e você precisa/precisou prestar o serviço obrigatório'''

# Prova

nome = input("Informe seu nome: ")
nota = float(input("Digite sua nota de 0 a 10: "))
if nota == 10:
  print (f"{nome}, você é o bichão mermo...")
elif (nota >= 6 and nota < 10):
  print(f"{nome}, bom trabalho")
else:
  print("Burro, não tirou dez...")
