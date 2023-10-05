"""Exercício Python 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50."""

print('{:=^40}'.format('Números Pares'))

for c in range(1, 50+1): #50+1 para que o número 50 seja considerado, caso não houvesse o +1 iria somente  até o 49

    if c%2 == 0: # se o resto de c/2 for 0
        print(f'Arca: {c} é PAR')

