"""Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
dessa progressão."""

cores = {'limpa':'\033[m',
         'green':'\033[32m'}



import math

print('{:=^40}'.format('Progressão Aritmética'))

termo = int(input('Arca:Informe o primerio termo desejado:'))
razão = int(input('Arca: Informe a razão a ser utilizada:'))
decimo = termo +(10-1) * razão # Esta variavel é para que a progressão só vá até o 10° termo




print('\n\n\n\n\n','='*40)
print('{:^40}'.format('TERMOS DA PA'))
print('='*40)
for c in range(termo, decimo + razão, razão): # começa no termo,  vai até a soma da variavel 'decimo' e 'razão', e vai pulando de acordo com o valor dentro da variavel  razão
       print('{}'.format(c), end='->') # o end substitui as quebra de linha! nesse caso por setas
print('{}Acabou!{}'.format(cores['green'], cores['limpa'])) # aqui estamos deixando a palavra acabou da cor verde






