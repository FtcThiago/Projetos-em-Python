#DESAFIO 042

"""Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de
triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes"""

""" Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar 
um triângulo.
"""
#Cor

cores = {'clean':'\033[m',
         'red':'\033[34m',
         'blue':'\033[31m',
         'green':'\033[32m'}

import emoji

reta1 = float(input('Arca:Informe o tamanho da primeira reta:'))
reta2 = float(input('Arca:Informe o tamanho da segunda reta:'))
reta3 = float(input('Arca:Informe o tamanho da terceira reta:'))

valor1 = bool((abs(reta2-reta3)) < reta1 < (abs(reta2+reta3))) # abs() é usada para retornar o valor absoluto de um número, e este é o calcúlo para saber se conseguimos montar um triangulo.
valor2 = bool((abs(reta1-reta3)) < reta2 < (abs(reta1+reta3)))
valor3 = bool((abs(reta1-reta2)) < reta3 < (abs(reta1+reta2)))

if valor1==True or valor2==True or valor3==True:
    print(f'Arca:Os comprimentos da sua reta obedecem a regra para formar um Triângulo.{emoji.emojize(":red_triangle_pointed_up:")}')
    if reta1 == reta2 == reta1 == reta3: # posso usar reta1 == reta2 == reta1 == reta3 OU reta1 == reta2 and  reta1 == reta3
        print('Arca:Esse é um triângulo {}EQUILÁTERO{},pois todos os seus lados são iguais!'.format(cores['red'], cores['clean']))
    elif reta1== reta2 or reta1== reta3 or reta2== reta3:
        print('Arca:Esse é um triângulo {}ISÓCELES{},pois dois de seus lados são iguais!'.format(cores['green'], cores['clean']))
    elif reta1 != reta2 and reta3 or reta2 != reta3:# posso usar reta1 != reta2 != reta3 != reta1 OU reta1 != reta2 and reta3 or reta2 != reta3
        print('Arca:Esse é um triângulo {}ESCALENO{},pois nenhum de seus lados são iguais'.format(cores['blue'], cores['clean']))
else:
    print(f'Arca:Os valores informados não obedecem a regra para montar um triângulo{emoji.emojize(":exclamation_question_mark:")}')