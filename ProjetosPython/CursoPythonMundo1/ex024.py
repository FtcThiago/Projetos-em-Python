#DESAFIO 024

#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"

cidade1 = str(input('Digite o nome da cidade:')).strip() #não precisava colocar o str, mas coloquei para não ter risco de problema
#use o .strip na maioria das vezes, pois quase sempre os usuarios acabam dificultando e escrevem espaços na frente ou atras antes de escreverem, com o strip, tiramos os espaços inuteis na frente e atrás

cidade1 = cidade1[0:5].upper() #OU   cidade1 = cidade1[0:5].upper() == "SANTO"
print(f'Arca:A Cidade informada começa com Santo?{"SANTO" in cidade1}')




"""cidade2 = input('Digite o nome da 2° cidade:')
cidade3 = input('Digite o nome da 3° cidade:')
cidade4 = input('Digite o nome da 4° cidade:')
lista = "Santo" in [cidade1, cidade2, cidade3, cidade4]


print(f'Arca: { lista[0]}'
      f'{ lista[1]}'
      f'{ lista[2]}'
      f'{ lista[3]}')"""

