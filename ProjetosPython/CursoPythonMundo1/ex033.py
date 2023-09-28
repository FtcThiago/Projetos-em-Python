#DESAFIO 033

#033 Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = float(input('Arca:Informe um número qualquer.Primeiro número:'))
num2 = float(input('Arca:Informe um número qualquer.Segundo número:'))
num3 = float(input('Arca:Informe um número qualquer.Terceiro número:'))

menor = num3
maior = num3

#Menor
if num1 < num2 and num1 < num3:
    menor=num1
if num2 < num1 and num2 < num3:
    menor = num2

#Maior
if num1 > num2 and num1 > num3:
    maior = num1
if num2 > num1 and num1 > num3:
    maior = num2
print(f'O menor Número é o: {menor:.0f}')
print(f'O maior Número é o: {maior:.0f}')







