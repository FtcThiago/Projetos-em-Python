"""Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas
já são maiores.
"""
from datetime import date
import time
# listaNome = [] #lita que recebera os 7 nome digitados dentro do for
# listaAno = []
# for c in range(1,7+1):
#     nome = input('Arca:Informe seu nome:')
#     ano = int(input('Arca:Informe seu ano de nascimento:'))
#     listaNome.append(nome) #o append guarda os nomes dentro da lista
#     listaAno.append(ano)
#
# for i in listaNome:
#     listaAno.append(i)
#
#
# print(listaAno)



menor = 0
maior = 0


for c in range(1, 7+1):
    ano = int(input(f'Arca:Informe o ano de nascimento da {c}° pessoa:'))
    idade = date.today().year - ano

    if idade > 21:
        maior += 1
    else:
        menor += 1

print(20*'=')
print(f'Arca: Das sete pessoas, {maior} são de maiores e {menor} são menores!')
print(20*'=')