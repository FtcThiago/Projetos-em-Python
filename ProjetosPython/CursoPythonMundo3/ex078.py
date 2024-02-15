"""Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. """

posiçaoMe = posiçaoMa = numeros = list()


for c in range(0, 5): #O usuário irá informar cinco valores.

    numeros.append(int(input(f'Arca:Informe o valor na posição {c}°:')))#A lista está recebendo os valores digitado
                                                                        # pelo usuário



print('='*30)
print(f'Arca:Você digitou os valores {numeros}')
print(f'Arca:O maior valor foi o {max(numeros)} e está nas posições ', end='')
for pos, v in enumerate(numeros): # Condição para achar a posição de todos os valores.

    if v == max(numeros):# Se chegar na posição do maior valor, então ele será mostrado
        print(pos, '...' , end='')

    if pos == 5:#Após ter passado por todos os valores, quando o pos encontrar a posição cinco(a última) ele fecha
        break


print(f'\nArca:O menor valor foi o {min(numeros)} e está nas posições ', end='')
for pos, v in enumerate(numeros):

    if v == min(numeros):#Se chegar na posição do menor valor, então ele será mostrado
       print(pos, '...', end='')


    if pos == 5: #Após ter passado por todos os valores, quando o pos encontrar a posição cinco(a última) ele fecha
        break
