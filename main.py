# Primeiro projeto Python
'''print ("Hello World!")

nome = 'Thales Gabriel'
idade = 22

print(nome)'''

#Sistema de votos
import os

votos_Lula = 0
votos_Bolsonaro = 0

while True:
  print('-'*20)
  print('Total Lula:',votos_Lula)
  print('Total Bolsonaro:',votos_Bolsonaro)
  print('-'*20)

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
  
  os.system('clear')