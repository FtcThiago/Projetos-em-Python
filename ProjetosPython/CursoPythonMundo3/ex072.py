""" Exercício Python 072: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""


print('{:=^40}'.format('Números por extenso'))


#
# numExtenso=('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
#             'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
#
# numero = 0
#
# numero = int(input('Arca:Informe um número entre 0 e 20:'))
#
# if numero < 0 or numero > 20: #Função para caso o usuário digite errado
#     while numero < 0 or numero > 20:
#         numero = int(input('Arca:Tente novamente!Arca:Informe um número entre 0 e 20:'))
#
#
# print('{:=^40}'.format(''))
# print(f'Arca:O número escolhido foi o {numExtenso[numero]}') # A tupla devolve o valor contido na posição tal de
#                                                              # acordo com o que foi digitado pelo usuário, e no caso,
#                                                              #o número digitado pelo usuário está sendo utilizado
#                                                 #como parâmetro para achar dentro da tupla o valor em sua posição.




#Jeito do Professor guanabara abaixo


numExtenso=('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')



opcao = 0
while True:

    num = int(input('Arca:Informe um número entre 0 e 20:'))

    if num >= 0 and num <= 20:
        print(f'Arca: Você escolheu o número {numExtenso[num]}')

        print('{:=^40}'.format(''))
        opcao= int(input('Arca:Deseja continuar?'
                         '\n[1] SIM'
                         '\n[2] NÃO'))
        if opcao == 2:
            break
    else:
        print('Arca:Tente Novamente!', end='')







