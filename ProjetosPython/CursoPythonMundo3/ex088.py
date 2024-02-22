"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em
uma lista composta."""

print('{:=^40}'.format(''))
print('{:^40}'.format('Jogo da Mega Sena'))
print('{:=^40}'.format(''))

from random import sample
from time import sleep
palpites = []


palpites.append(int(input('Arca:Informe quantos jogos deseja fazer:')))#Usando a lista palpites para receber temporariamente a quantidade de jogo que o usuário vai querer.

for c in range(0,palpites[0]):# de 0 até o número digitado pelo usuário

    palpites.append(sample(range(1,60),6)) # a lista palpite vai receber 6 números aleátorios de 1 a 60.


print('-='*35)
print(f'Arca:Você escolheu palpites para {palpites[0]} jogos.'
      f'\nArca:Processando os palpites...')
for c in range(0,palpites[0]+1): #de 0 até o número digitado pelo usuário, o mais um porque a posição zero não será considerada, pois a posição zero é o número digitado pelo usuário.
    if c != 0:
        palpites[c].sort()
        print(f'{c}° jogo - {palpites[c]:}')
        sleep(2)
del palpites[0]#

print('{:=^40}'.format('Boa sorte'))