"""  Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

print('{:=^40}'.format('Extraindo valores da lista'))

lista = list()
opçao = ""

while True:
    lista.append(int(input('Arca:Informe algum número:'))) #Recebendo valor do usuário e guardando na lista

    while True: # o while quebra se a opção break for acionada
        opçao = str(input('Arca:Deseja continuar?[S/N]'))

        if opçao != 'S' and opçao !='s' and opçao != 'N' and opçao != 'n': #Se o valor inserido pelo usuário for
            print('Valor inválido!')                            # diferente de S,s,N ou n , ele não saira do while
        if opçao in 'NnSs': # Se a opção for S,s,N ou n, o break irá quebrar o while
            break
    if opçao in 'Nn': # Se a opção for o n, ele entra no primeiro break, e já cai nesse break de baixo.
        break


print('='*40)
print(f'Arca:Os números digitados foram {lista}, ao total {len(lista)} números') #O len() para saber quantos valores foram digitados
lista.sort(reverse=True) #.sort(reverse = True) para ordenar os números de forma decrescente
print(f'Arca:Lista em forma decrescente {lista}')
if lista.count(5) >=1:
    print(f'Arca: O valor cinco está na lista e foi digitado {lista.count(5)} vezes') #.count para mostrar quantas vezes o número cinco apareceu
else:
    print('Arca: O valor cinco não está na lista.')


