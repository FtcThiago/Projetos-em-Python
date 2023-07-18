# DESAFIO 020

# Arca:Importando módulo random( que serve(acredito que não so para isso) para escolher aleatoriamente algo)
from random import shuffle,sample  #shuffle serve para embaralhar o que tem na lista e o sample é para não repetir nenhum nome

n1 = input('Qual o nome do Aluno 1:')
n2 = input('Qual o nome do Aluno 2:')
n3 = input('Qual o nome do Aluno 3:')
n4 = input('Qual o nome do Aluno 4:')
lista = [n1, n2, n3, n4]
shuffle(lista)
ordemApres = sample(lista, 4)
# neste caso eu só precisava usar  ou o shuffle ou o sample....que dara o mesmo resultad! no entanto coloquei os dois para explicar o que fazem

print('----------------------------------------')
print(f'Arca:O professor deseja sortear aleatoriamente a ordem de apresentação dos alunos.'
      f'\nArca:Ordem das apresentações:{ordemApres}')
      #f'\nPrimeiro a apresentar:{random}'
      #f'\nSegundo a apresentar:{random}'
      #f'\nTerceiro a apresentar:{random}'
      #f'\nQuarto a apresentar:{random}')

print('----------------------------------------')
