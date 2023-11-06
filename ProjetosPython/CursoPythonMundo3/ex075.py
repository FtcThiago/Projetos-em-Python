"""Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em
uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""
numero = pares = 0
tupla = (int(input('Informe o 1° Valor:')), int(input('Informe o 2° Valor:')), int(input('Informe o 3° Valor:')), int(input('Informe o 4° Valor:')), int(input('Informe o 5° Valor:')))
#Ai encima, é uma Tupla recebendo os valores digitados! coloquei um input dentro de cada posição dela,e assim ela recebe os valores que o usuário digitar.

print('{:=^40}'.format(''))
print(f'Arca: Os valores informados foram{tupla}')

print('{:=^40}'.format(''))

print('Arca:Os números pares digitados foram:', end='')
for c in tupla:

    if c %2 ==0:# #Condição para achar o número Par
        print(c, end=' ')
print(f'\nArca:O valor 9 apareceu {tupla.count(9)} vezes!')

if tupla.count(3) > 0: # condição para que caso não seja digitado o número três, não aja problema no programa
    print(f'Arca:O primeiro número 3 digitado está na posição {tupla.index(3) + 1}') # O comando index está
    # responsável por achar em qual posição está o primeiro número três que ele encontrar, e esse +  é para que
    # seja mostrado a posiçaõ do três sem levar em consideração a posição zero,ou seja, se o três está no posição 3, logo ele deve ser mostrado na posição 4.

#Outro modo de analisar se o valor três foi digitado: Modo do professor guanabara
#
#if 3 in numero:
#    print(f'Arca:O primeiro número 3 digitado está na posição {tupla.index(3) + 1}')


