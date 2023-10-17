'''Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os
N primeiros elementos de uma Sequência de Fibonacci. '''

print('{:=^40}'.format('Sequência de Fibonacci'))


cores = {'limpa':'\033[m',
         'azul':'\033[34m'}

numero = int(input('Arca:Apartir de qual número você deseja começar a sequência de fibonacci?'
                   '\nDigite:')) #Variável para saber de qual número começar a sequência de fibonacci
numero3 = numero # variável que será essencial para que a sequência de fibonacci possa ocorrer; como um pêndulo, ela representará uma das bolas e a variável numero representará a outra( pêndulo é  aquela balança de bolinhas que bate uma na outra até que a perda de energia as faz parar; metaforicamente a variável termo representa a perda de energia, pois a sequência acaba de acordo com seu valor.)
termo = int(input('Arca:Quantos termos você deseja mostrar:')) # variável que determina até aonde a sequência vai chegar
print('{:=^40}'.format(''))
print('{:^40}'.format('Sequência Fibonacci'))
print('{:=^40}'.format(''))
c = 0

while c != termo/2: # tive que dividir o termo por dois pois usei duas variáveis para que a sequência pudesse ser feita, logo se o usuário pedisse 10 termos, iria aparecer 20; por isso divido por 2.
    c = c+1

    print('{}{},{}{},'.format(cores['azul'], numero3, numero, cores['limpa']), end='')
    numero3 = numero3 + numero # se o usuario escolher o numero 1, então numero3 = 1 + 1
    numero = numero3 + numero # numero = 2 + 1
    # E assim ,com essas duas variávies e calculo eu consegui montar a sequência de fibonacci


