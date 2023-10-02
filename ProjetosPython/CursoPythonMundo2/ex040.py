#DESAFIO 040

"""Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma
mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO"""


#CORES

cores = {'limpa':'\033[m',
         'Red':'\033[31m',
         'amarelo':'\033[33m',
         'azul':'\033[34m'}


print(20*'{}_{}'.format(cores['azul'], cores['limpa']))
nota = float(input('Arca:Informe a primeira nota:'))
nota1 = float(input('Arca: Informe a segunda nota:'))
print(20*'{}_{}'.format(cores['azul'], cores['limpa']))
media = (nota+nota1)/2



if media < 5.0:
    print('Arca:Você está  {}REPROVADO{}, com uma média abaixo de 5.0.'
          '\n1°:{}'
          '\n2°:{}'
          '\nMédia:{}'f'{media}'.format(cores['Red'], cores['limpa'], nota, nota1, cores['Red']))
elif media >=5.0 and media<=6.9:
    print('Arca:Você está de {}RECUPERAÇÃO{},com a média entre 5.0 e 6.9'
          '\n1°:{}'
          '\n2°:{}'
          '\nMédia:{}'f'{media}'.format(cores['amarelo'], cores['limpa'], nota, nota1, cores['amarelo'] ))
else:
    print('Arca:Você está {}APROVADO{}, com uma média 7 ou superior'
          '\n1°:{}'
          '\n2°:{}'
          '\nMédia:{}'f'{media}'.format(cores['azul'], cores['limpa'], nota, nota1, cores['azul']))
