"""  Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será
interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""



print('{:=^40}'.format('Jogo de Par ou Ímpar'))

from time import sleep
from random import randint

numero = 0
numeroArca = 0
escolha = 0
tot = 0
resultado = 0
c = ''

print('Arca:Vamos jogar o jogo de Par ou ímpar. Escolha um número!')
while  True:
    print('{:=^40}'.format(''))
    numeroArca = randint(0, 10)

    numero = int(input('Arca:Escolha um número:'
                       '\nDigite:'))

    escolha = int(input('Arca: Escolha Par ou ímpar:'
                        '\n[1] Par'
                        '\n[2] ímpar'))
    resultado = numero + numeroArca
    print(numeroArca)
    print(resultado%2)
    print('{:=^40}'.format(''))
    print('Arca: Preparado? Vamos lá!')
    print('Arca: PAR')
    sleep(1)
    print('Arca:OU')
    sleep(1)
    print('Arca:ÍMPAR')
    sleep(2)

    if escolha == 1:
        c = 'Par'
    elif escolha == 2:
        c = 'Ímpar'


    if resultado % 2 == 0:
         if escolha == 1:
            tot = tot + 1
            print('Arca:Você ganhou! Vamos mais uma vez!')

         elif escolha == 2:
             print('Arca:Você perdeu!Finalizando....')
             break

    if resultado % 2 == 1:
        if escolha == 2:
            tot = tot + 1
            print('Arca:Você ganhou!Vamos mais uma vez!')

        elif escolha == 1:
            print('Arca:Você perdeu!Finalizando....')
            break



    print(f'Arca:Eu escolhi {numeroArca} e você {numero}! Logo {resultado} é um número {c}')

print('{:=^40}'.format(''))
print(f'Arca:Eu escolhi {numeroArca} e você {numero}! Logo {resultado} é um número {c}')
print(f'Arca: Você teve cerca de {tot} vitórias consecutivas antes de errar')