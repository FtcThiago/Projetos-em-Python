"""Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""


import datetime


nomeMulher = []
mediaIdades = 0
idade = 0
mulheresVinte=0
nomeHomem = ''
idadeHomem = 0
for c in range(1, 4+1):
    print('{:=^40}'.format(f'{c}° Pessoa'))
    nome = input(f'Informe seu nome:')
    ano = int(datetime.date.today().year-int(input(('Informe seu ano de nascimento:'))))
    sexo = int(input('Informe seu sexo:'
                 '\n[1] Masculino'
                 '\n[2] Feminino'))

    idade = idade + ano

    if sexo == 1:
        if ano > idadeHomem or ano == idadeHomem:
            nomeHomem = nome
            idadeHomem = ano

    if sexo == 2 and ano<20:
        nomeMulher.append(nome)
        mulheresVinte = mulheresVinte + 1


    # idade = ano + idade
mediaIdades = idade/4



print('\n',20*'=')
print(f'Arca: A media de idade de todos os participantes é de : {mediaIdades}'
      f'\nArca: O homem mais velho se chama {nomeHomem} com a idade de {idadeHomem}'
      f'\nArca: há {mulheresVinte} mulhere(s) com menos de 20 anos. ')

if mulheresVinte > 0:
    print(f'\nLista dos nomes das mulheres:{nomeMulher}')


print(20*'=')
