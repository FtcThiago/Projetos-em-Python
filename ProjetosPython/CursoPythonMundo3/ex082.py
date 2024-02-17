"""Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas."""



impar = list()
valores = list()
par = list()
opçao = ''

while True:

    valores.append(int(input('Arca:Informe um número:'))) #Lista recebendo os valores digitados pelo usuário

    while True:

        opçao = input('Arca:Deseja continuar?[S/N]')

        if opçao != 'S' and opçao != 's' and opçao != 'N' and opçao != 'n':  # Se o valor inserido pelo usuário for
            print('Valor inválido!')
        if opçao in 'NnSs': # Se o usuário escrever o S,s,N ou n ele saí do while ele quebra o while e volta pro while principal
            break

    if opçao in 'Nn': #Se o usuário escolher o N,n ele quebra o laço do while principal e encerra o programa
        break

for c in valores: #Condição para analisar se os valores dentro da lista são Pares ou Ímpares

    if c % 2 == 0: # Condição para achar os números Pares
        par.append(c)

    if c % 2 == 1: #Condição para achar os números Ímpares
        impar.append(c)

print('='*60)
print(f'Arca:Lista completa {valores}')
print(f'Arca:Lista de pares {par}')
print(f'Arca:Lista de ímpares {impar}')