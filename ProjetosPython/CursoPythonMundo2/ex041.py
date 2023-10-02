#DESAFIO 041

"""Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER"""

from datetime import date

#Cores

cores = {'limpa':'\033[m',
         'Red':'\033[31m',
         'azul':'\033[34m',
         'verde':'\033[32m',
         'ciano':'\033[36m',
         'roxo':'\033[35m'}

print(20*'{}_{}'.format(cores['azul'], cores['limpa']))
ano = int(input('Arca:Informe seu ano de nascimento:'))
print(20*'{}_{}'.format(cores['azul'], cores['limpa']))

idade = date.today().year - ano
categoria = ['Mirim', '\nInfantil', '\nJunior', '\nSênior', '\nMaster']

print(f'Arca:idade do Atleta: {idade}')
if idade <= 9:
    print('Arca:Sua categoria é: {}{}{}'.format(cores['Red'], categoria[0], cores['limpa']))
elif idade <= 14:
    print('Arca:Sua categoria é: {}{}{}'.format(cores['verde'], categoria[1], cores['limpa']))
elif idade <= 19:
    print('Arca:Sua categoria é: {}{}{}'.format(cores['azul'], categoria[2], cores['limpa']))
elif idade <= 25:
    print('Arca:Sua categoria é: {}{}{}'.format(cores['ciano'], categoria[3], cores['limpa']))
elif idade > 25:
    print('Arca:Sua categoria é: {}{}{}'.format(cores['roxo'], categoria[4], cores['limpa']))
