#DESAFIO 043

"""Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de
Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida"""



from math import pow

#CORES

cores = {'limpa': '\033[m',
         'Red' :'\033[31m',
         'amarelo':'\033[33m',
         'ciano':'\033[36m',
         'verde':'\033[32m',
         'azul':'\033[34m'}

print(20*'{}_{}'.format(cores['azul'],cores['limpa']))
peso = float(input('Arca:Informe o seu peso (kg):'))
altura = float(input('Arca:Informe a sua altura (m):'))
print(20*'{}_{}'.format(cores['azul'],cores['limpa']))

imc = float(peso/(pow(altura, 2)))
categoria = ['Abaixo do Peso', 'Peso Ideal', 'Sobrepeso', 'Obesidade', 'Obesidade mórbida']
if imc < 18.5:
    print('Arca:Status:{}{}{}'
          '\nArca:Coma mais :)'.format(cores['Red'], categoria[0], cores['limpa']))
elif 18.5 <= imc <25:
    print('Arca:Status:{}{}{}'
          '\nArca:ótimo'.format(cores['amarelo'], categoria[1], cores['limpa']))
elif 25 <= imc <30:
    print('Arca:Status:{}{}{}'
          '\nArca:ainda não ha perigo, mas busque uma alimentação saudável'.format(cores['ciano'], categoria[2], cores['limpa']))
elif 30 <= imc <40:
    print('Arca:Status:{}{}{}'
          '\nArca:Cuidado!cuide de sua saúde,procure fazer exercícios e se alimentar bem '.format(cores['verde'], categoria[3], cores['limpa']))
elif imc >40:
    print('Arca:Status:{}{}{}'
          '\nArca:Cuidado! Seu peso pode causar sua morte,procure um médico'.format(cores['ciano'], categoria[4], cores['limpa']))

print(f'Arca: Seu IMC é {imc:.2f}')