'''Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só
vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''


print('{:=^40}'.format('Soma entre números'))

cores = {'limpa':'\033[m',
         'verde':'\033[32m'}


c = soma = 0

print('Arca: Informe um número inteiro OU Digite [999] para terminar o programa!')
while c != 999:
    numero = int(input('Digite:'))
    c = numero
    if numero != 999:
        soma = soma + numero

print('{:=^20}'.format(''))
print('Arca:A soma entre os números digitados foi de {}{}{}'.format(cores['verde'], soma, cores['limpa']))