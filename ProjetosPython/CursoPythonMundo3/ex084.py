"""Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma
lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""


print('{:=^60}'.format('Maior e Menor pesos-Listas dentro de Listas'))

#=============================================================
pessoas = list()
pessoa = list()
pesadas = list()
leves = list()
opçao = ''


#=============================================================
while True:
    pessoa.append(str(input('Arca:Informe seu nome:')))
    pessoa.append(float(input('Arca:Informe seu peso:')))
    pessoas.append(pessoa[:]) #Lista pessoas recebendo valores da lista pessoa.
    pessoa.clear() # limpando dados da lista pessoa.




    #===============================================================
    opçao = ''#Zerando variável opção para que a condição consiga voltar para o while embaixo.
    while opçao != 'S' and opçao != 's' and opçao != 'N' and opçao != 'n' :
        print('-='*20)
        opçao = str(input('Arca:Deseja continuar?[S/N]'))

        if opçao in 'SsNn':
            break
        else:
            print('Opção Inválida!informe novamente.')
    print('-='*20)
    if opçao in 'Nn':
        break
#============================================================
for v in pessoas: #Condição para identificar os nomes das pessoas mais pesadas e mais leves.
    variavel = v[1] #variável criada para que a lista pessoa conseguise receber o valor inteiro da lista pessoa,isto é, o peso
    pessoa.append(variavel) #Lista pessoa recebendo os valores inteiros da lista pessoas atraves da variável; E reutilizando a lista pessoa.

for v in pessoas:
    variavel = v[1]

    if variavel == max(pessoa):
        pesadas.append(v[0][:])
    elif variavel == min(pessoa):
        leves.append(v[0][:])







#============================================================
print('-='*60)
print(f'Arca:Lista de todas as pessoas e seus respectivos pesos: {pessoas}')
print(f'Arca:Ao todo foram cadastradas {len(pessoas)} pessoas')
print(f'Arca:O maior peso lido foi o de {max(pessoa):.1f}Kg.Peso de: ', end='')
for c in pesadas:
    print(c.title(),'...',end='')
print(f'\nArca:O menor peso lido foi o de {min(pessoa):.1f}Kg.Peso de: ', end='')
for c in leves:
    print(c.title(),'...',end='')