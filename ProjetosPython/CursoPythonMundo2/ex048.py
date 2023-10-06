"""Exercício Python 048: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
intervalo de 1 até 500."""

cores = {'limpa':'\033[m',
        'green':'\033[32m'}


print('{:=^40}'.format('Números Ímpares'))
soma = 0

for c in range(1, 500+1): # 500+1 par aque o número 500 seja considerado
    if c % 2 == 1 and c % 3 == 0: # se o resto de c%2 for 1 e c%3 for 0
        soma = c + soma

        print('Arca: {}{}{} é um número Ímpar e múltiplo de 3'.format(cores['green'], c, cores['limpa']))

print('A Soma entre Todos esses números é :{}{}{}'.format(cores['green'], soma, cores['limpa']))