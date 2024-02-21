"""Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta."""

print('{:=^40}'.format('Matriz de 3x3'))

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #colocando três valores dentro das três listas dentro da lista principal!


for c in range(0, 3):
    for i in range(0, 3):
        matriz[c][i] = int(input(f'Arca: Informe um valor para [{c},{i}]:')) #Recebendo valor do usuário e preenchendo todos os valores dentro das listas.



print('-='*60)
for c in range(0,3):
    print()
    for i in range(0,3):
        print(f'[{matriz[c][i]:^5}]', end='')#Mostrando um por um os valores dentro das listas que estão na
                                             #lista principal(a matriz).
                                             #Os simblos :^5  é para centralizar o que será mostrado.


