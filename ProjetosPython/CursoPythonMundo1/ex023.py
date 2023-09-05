#DESAFIO 023

#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Informe um número inteiro qualquer:'))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10



print(f'Arca:O número informado foi {numero}'
      f'\nArca:A unidade:{u}'
      f'\nArca:A dezena:{d}'
      f'\nArca:A centena:{c}'
      f'\nArca:O milhar: {m}')

