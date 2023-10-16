''' Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''


print('{:=^40}'.format('Fatorial!'))
from time import sleep

import math


cores = {'limpa':'\033[m',
         'roxo':'\033[35m',
         'verde':'\033[32m'}



numero = 1
fatorial = 0

numero = int(input('Arca:Informe o número desejado:'))
print('{:=^10}'.format(''))
fatorial = math.factorial(numero)

print('{}{}!{} = '.format(cores['roxo'], numero, cores['limpa']), end='')
while numero != 0:


    print('{}{}{}'.format(cores['verde'],numero,cores['limpa']), end='')
    print(' X ' if numero > 1 else ' = ', end='') #Se eu não fisse esse condição do if, o resultado seria apresentado assim ;ex: 5! = 5x4x3x2x1x = 120, só que com essa condição ele aparece 5! = 5x4x3x2x1 = 120
    numero = numero - 1

    if numero == 0:
        print('{}{}{}'.format(cores['verde'], fatorial, cores['limpa']))



#Mesmo exercício com o for

print('{:=^40}'.format(''))
print(' Mesmo programa Usando o For')
sleep(2)


numero = int(input('Arca:Informe o número desejado:'))
print('{:=^10}'.format(''))
fatorial = math.factorial(numero)
c = 0

print('{}{}!{} = '.format(cores['roxo'], numero, cores['limpa']), end='')

for c in range(numero,0,-1):

    print('{}{}{}'.format(cores['verde'], numero, cores['limpa']), end='')
    print(' X ' if numero > 1 else ' = ', end='')  # Se eu não fisse esse condição do if, o resultado seria apresentado assim ;ex: 5! = 5x4x3x2x1x = 120, só que com essa condição ele aparece 5! = 5x4x3x2x1 = 120
    numero = numero - 1

    if numero == 0:
        print('{}{}{}'.format(cores['verde'], fatorial, cores['limpa']))


