"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o
vencedor tirou o maior número no dado."""

from random import randint #Importação para escolher números aleátorios
from operator import itemgetter #Importação para Ordenar um dicionário(pelo menos foi ela que foi usada para esse caso)
from time import sleep #Importação para usar times(tempos entre uma ação e outra)
jogador = {'jogador1':randint(1,6),'jogador2':randint(1,6),'jogador3':randint(1,6),'jogador4':randint(1,6)} #Criando um dicionário com 4 chaves e seus valores.


for k,v in jogador.items():#Mostrando as chaves e os valores dentro do dicionário jogador.
    print(f'{k} tirou {v} no Dado.')
print('-='*30)
print('{:=^30}'.format('Ranking'))
ranking = list()
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)#Criei a lista ranking que recebeu o dicionário jogador e o ordenou,ordenou atraves somente dos valores e não das Keys, por isso que nesse comando key=itemgetter(1) eu escolhi o 1 e não o zero.

for i,v in enumerate(ranking):#Já que o ranking é uma lista, eu precisei usar o enumerate para pegar seus indices(Keys).
    print(f'{i+1}° lugar:{v[0]} com o valor {v[1]}')
    sleep(1)



