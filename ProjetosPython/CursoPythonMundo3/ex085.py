"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista
 única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares
 em ordem crescente."""

print('{:-=^40}'.format(''))

variavel = 0
lista = [[], []] #Criando duas listas dentro de uma lista.


for c in range(0,7):
    variavel = int(input(f'Arca:Digite o {c+1}° número:')) #c+1 para que o valor zero não aparece, mas comece apartir do 1.

    if variavel % 2 ==0: #Se a variável for Par a primeira lista vai receber essa variável
        lista[0].append(variavel)
    else: #Senão! isto é, se a variável não for Par, ela é impar, então a segunda lista vai receber essa variável
        lista[1].append(variavel)

lista[0].sort()#Organizando em ordem crescente a primeira lista
lista[1].sort()#Organizando em ordem crescente a segunda lista
print('-='*60)
print(f'Arca: Os números Pares informados: {lista[0]}')
print(f'Arca: Os números Ímpares informados: {lista[1]}')






