#DESAFIO 039

"""Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua
idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo
do alistamento.Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""


from datetime import date



#COR

cores = {'limpa':'\033[m',
         'Red':'\033[34m'}



#------------------------------------------



print(20*'{}_{}'.format(cores['Red'],cores['limpa']))
ano = int(input('Arca:informe o ANO do seu nascimento:'))
print(20*'{}_{}'.format(cores['Red'], cores['limpa']))

anoAtual = date.today().year  #Pegando data atual, no caso só o ano por causa do year
idade = anoAtual-ano

print(f'Arca:Sua Idade é {idade}')
if idade < 18:
    saldo = 18-idade
    print(f'Arca:Você ainda deve se alistar!'
          f'\nArca: Você ira se alistar daqui há {saldo} anos, no ano de {anoAtual+saldo} ')
elif idade == 18:
    print(f'Arca: Você deve se alistar, este é o ano para seu alistamento')
else:
    saldo = idade - 18
    print(f'Arca:Você está atrasado em seu alistamento! '
          f'\nArca: Seu alistamento devia ter sido feito há {saldo} no ano de {ano-saldo}')