#DESAFIO 038

"""Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os.
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais"""

#CORES

cores = {'limpa' :'\033[m',
         'Red' :'\033[34m'}


#-----------------------------------------------------------

print(20*'{}-{}'.format(cores['Red'],cores['limpa']))
numero1 = int(input('Arca:Informe dois números inteiros:'
                   '\n1°Número:'))
numero2 = int(input('Arca:2°Número:'))
print(20*'{}-{}'.format(cores['Red'],cores['limpa']))
if numero1 > numero2:
    print(f'Arca:O primeiro número é maior que o segundo'
          f'\n1°:{numero1} '
          f'\n2°:{numero2}')
elif numero2 > numero1:
    print(f'Arca:O segundo número é maior que o primeiro'
          f'\n1°:{numero1} '
          f'\n2°:{numero2}')
else:
    print(f'Arca: Ambos os números digitados são iguais'
          f'\n1°:{numero1} '
          f'\n2°:{numero2}')
