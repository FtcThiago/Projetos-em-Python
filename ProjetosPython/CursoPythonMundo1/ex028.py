#Desafio 028

#028 Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random, time

numPc = random.randrange(0, 5)

print('----------'
      '\nArca:Irei escolher um número entre 0 e 5, tente adivinhar que número será:'
      '\n----------')
num = int(input('Arca:Escolha o número:'))
print("Arca:Processando...")
time.sleep(2)
if num == numPc:
    print(f'Arca:Muito Bem, você Venceu! Você escolheu {num} e eu escolhi o {numPc}')
else:
    print(f'Arca:Que pena, você Perdeu! Você escolheu {num} e eu escolhi o {numPc}')




