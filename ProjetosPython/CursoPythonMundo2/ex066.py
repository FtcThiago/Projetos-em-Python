''' Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai
parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''



print('{:=^64}'.format('Soma entre Números'))


cores = {'limpa':'\033[m',
         'azul':'\033[34m'}


soma = 0
c = 0
while True:


    numero = int(input('Arca:Informe um número! Digite [999] para interromper o programa'
                       '\nDigite:'))
    print('{:-^40}'.format(''))

    if numero == 999:# Essa condição tem que ficar antes do cálculo da soma, para que o 999 não seja somado junto!
        break

    soma += numero
    c += 1


print('Arca:Foram digitados {}{}{} números!E a soma entre os números é de:{}{}{}!'.format(cores['azul'], c, cores['limpa'], cores['azul'], soma, cores['limpa']))