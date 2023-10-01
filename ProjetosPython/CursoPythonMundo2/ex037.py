#DESAFIO 037

"""Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o
usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""

numero = int(input('Arca:Digite um número inteiro:'))
opção = int(input('Arca:Escolha a conversão desejada:'
                    '\n[ 1 ] converter para  BINÁRIO'
                    '\n[ 2 ] converter para OCTAL' 
                    '\n[ 3 ] converter para HEXADECIMAL'
                    '\nEscolha sua opção:'))


if opção == 1:
    print(f'Arca: O número {numero} em Binário é : {bin(numero)[2:]}') #bin()  transformar o número em binário,o [2:] é a manipulação de texto, afim de ,neste caso, mostrar o valor a partir da posição 2 adiante

elif opção == 2:
    print(f'Arca: O número {numero} em Octal é: {oct(numero)[2:]}') # oct() transformar o número em octal, o [2:] é a manipulação de texto, afim de ,neste caso, mostrar o valor a partir da posição 2 adiante

elif opção == 3:
    print(f'Arca: O número {numero} em Hexadecimal é: {hex(numero)[2:]}') # hex() transformar o número em hexadecimal,o [2:] é a manipulação de texto, afim de ,neste caso, mostrar o valor a partir da posição 2 adiante

else:
    print('Arca:Opção inválida!Tente novamente')