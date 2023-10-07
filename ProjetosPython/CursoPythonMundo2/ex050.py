"""Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for ímpar, desconsidere-o."""

print('{:=^40}'.format('Cálculo com Pares'))

print('Arca:Informe 6 Números inteiros!')
listaNumero = [ ]
for c in range(1, 6+1):
    numero = int(input(f'Arca:Informe o {c}° número:'))
    if numero%2 == 0:
        listaNumero.append(numero) #Acrescentando a lista a váriavel numero


print(20*'=')
print('Arca: Foram selecionados apenas os números Pares!'
      f'\nArca:{listaNumero}'
      f'\nArca:A soma desses números Pares :{sum(listaNumero)}')
