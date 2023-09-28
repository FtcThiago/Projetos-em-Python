#DESAFIO 032

#032 Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

import calendar,datetime   #Com o modulo calendar consegui importar o comando isleap(para achar ve se o ano é bissexto em True ou False)
                           #Com o modulo datetime consegui baixar a data e hora atual do meu computador.

ano = int(input('Arca:Informe o ano:'))

if ano == 0:
    ano=datetime.date.today().year #o datetime está pegando a data de hoje(e com o year,está pegando so o ano no caso)
if calendar.isleap(ano)== True:
    print(f'Arca:O ano {ano} é um ano Bissexto')
else:
    print(f'Arca:O ano {ano} não é um ano Bissexto')
