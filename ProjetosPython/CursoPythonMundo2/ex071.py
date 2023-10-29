""" Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início,
 pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
 cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

cores = {'limpa':'\033[m',
         'roxo':'\033[35m',
         'amarela':'\033[33m',
         'vermelha':'\033[31m',}



print('{:=^40}'.format('CAIXA ELETRÔNICO'))
from time import sleep

numero = cedulas50 = cedula20 = cedula10 = cedula1 = 0


while True:
    numero = int(input('Arca:Que valor você quer sacar:'))
    cedulas50 = numero // 50 # //  ->divisão inteira ; Vamos usar como exemplo se o valor para sacar vai se de R$1025, então o resto da divisão de 1025 // 50 é 20 ; 20 notas de R$50
    cedula20 = (numero - (cedulas50*50))//20 # (1025 - ( 20*50))//20 --> (1025 - 1000)// 20 --> 25//20 = logo a divisão inteira de 25 por 20 é 1 ; 1 nota de R$20
    cedula10 = (((numero - (cedulas50*50))-(cedula20*20)))//10 # (((1025 - (20*50))-(1*20)))//10 --> ((1025 - 1000)-20))//10 --> (25-20)//10 --> 5//10 = logo a divisão inteira de 5 por 10 é 0 ; 0 notas de R$10
    cedula1 = (((numero - (cedulas50*50))-(cedula20*20)))/1 # (((1025 - (20*50))-(1*20)))//10 --> ((1025 - 1000)-20))//10 --> (25-20)//10 --> 5/1 = logo a divisão de 5 por 1 é 5 ; 5 notas de R$1

    # cedula = (numero - cedula10)//1
    break



print('{:=^20}'.format(''))
print('Sacando....')
sleep(2)

if cedulas50 !=0:
    print('Arca: {}{:.0f}{} cédula(s) de R$50'.format(cores['roxo'],cedulas50,cores['limpa']))
if cedula20 !=0:
    print( 'Arca: {}{:.0f}{} cédula(s) de R$20'.format(cores['amarela'],cedula20,cores['limpa']))
if cedula10 !=0:
    print('Arca: {}{:.0f}{} cédula(s) de R$10'.format(cores['vermelha'],cedula10,cores['limpa']))
if cedula1 !=0:
    print( f'Arca: {cedula1:.0f} cédula de R$1')

print(f'Arca:Valor total --- R${numero:.2f}')










# Essa maracutaia ai embaixo foi o calculo doido que fiz para que eu achasse o calculo  certo para o programa
#
#n = m = j = k= p = c= d= e= f=0
# n = numero//50
# m = n * 50
# j = numero - m
# k = j//20
# p = k * 20
# c = j - p
# d = c//10
# e = c/1
#
#
# print(n)
# print(m)
# print(j)
# print(k)
# print(p)
# print(c)
# print(d)
# print(e)
