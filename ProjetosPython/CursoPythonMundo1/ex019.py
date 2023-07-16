#DESAFIO 019


#Arca:Importando módulo random( que serve(acredito que não so para isso) para escolher aleatoriamente algo)
from random import choice
#Váriaveis
n1 = input('Digite o nome do primeiro aluno:')
n2 = input('Digite o nome do segundo aluno:')
n3 = input('Digite o nome do terceiro aluno:')
n4 = input('Digite o nome do quarto aluno:')
lista = [n1, n2, n3, n4]




print(f'Arca:O professor deseja sortear entre os quatro alunos:{n1},{n2},{n3} e {n4} para apagar o quadro.'
      f'\nArca:Atraves do sistema,os alunos serão sorteados aleatoriamente:'
      f'\nArca:O aluno escolhido é:{choice(lista)}')#Com o random.choice() eu consigo escolher aleatoriamente algo dentro da lista que criei(lista)
print('----------------------------------------')