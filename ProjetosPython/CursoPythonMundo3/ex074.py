""" Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
 Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla."""

print('{:=^40}'.format('Gerando Números Aleatórios'))



import random

c = 0
tupla = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),  )


numMaior = tupla[0] #Começando com o primeiro valor, para que possa descobrir mais a frente qual o menor e maior número
numMenor = tupla[0]

while c != 5:


    if tupla[c] > numMaior: #uma condição que é capaz de analisar todos os cinco valores dentro da tupla e compara-los com as variáveis numMaior e numMenor, tudo isso graças ao parâmetro atráves da variável c.
        numMaior = tupla[c]
    if tupla[c] < numMenor:
        numMenor = tupla[c]

    c = c+1

    #OU Podemos fazer assim: Modo do professor guanabara
    #
    #print(f'O maior valor foi o {max(tupla)}')
    #print(f'O menor valor foi o {min(tupla)}')


print(f'Arca: Os números escolhidos foram: {tupla}')
print(f'Arca: O maior número foi o {numMaior}'
      f'\nArca: O menor número foi o {numMenor}')








