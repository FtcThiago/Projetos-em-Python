"""Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for."""

print('{:=^40}'.format('Tabuada'))

numero = int(input('Arca:Informe o número da tabuada desejada:'))

operacao = int(input('Arca:Informe a operação desejada:'
                         '\n[1] Multiplicação'
                         '\n[2] Divisão'
                         '\n[3] Soma'
                         '\n[4]Subtração'
                         '\nArca: Informe:'))

print(20*'=')
print(f'Arca:A tabuada escolhida foi a do {numero}')

for c in range(1, 10+1):
    if operacao == 1:
        print(f'{numero} X {c} = {c*numero}')
    elif operacao == 2:
        print(f'{numero} / {c} = {c/numero}')
    elif operacao == 3:
        print(f'{numero} + {c} = {c+numero}')
    elif operacao == 4 :
        print(f'{numero} - {c} = {c-numero}')

