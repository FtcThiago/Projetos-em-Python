'''  Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando a estrutura while.'''

"""Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
dessa progressão."""


cores = {'limpa':'\033[m',
        'verde': '\033[32m'}



print('{:=^41}'.format('Progressão Artimética com While'))

termo = int(input('Arca:Informe o primeiro termo da progressão:'))
razão = int(input('Arca:Informe a razão desejada:'))
print('{:=^41}'.format(''))
print('{:^41}'.format('TERMOS DA PA'))
print('{:=^41}'.format(''))
progressao = termo
c = 0

while c != 10:
    print(f'{termo},', end='')
    termo = termo + razão
    c = c + 1
print('{}Acabou!{}'.format(cores['verde'], cores['limpa']))