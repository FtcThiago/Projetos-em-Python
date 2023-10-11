''' Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''


cores = {"limpa":"\033[m",
         "azul":"\033[34m",
         "vermelho": "\033[31m",
         "verde":"\033[32m"}




print('{:=^40}'.format('{}Menu{} {}para{} {}Números{}').format(cores["azul"],cores["limpa"],cores["vermelho"],cores["limpa"],cores["verde"],cores["limpa"]))

numero1 = numero2 = resultado = float  #criando três variáveis; numero1 e numero2 para receber os números escolhidos pelo usuário ; A variável resultado para receber os resultados de cada operação, dependendo da escolha dos usuário, essa variável não é usada para ficar com os valores, ele os guarda temporariamente!
menu = int #variável para escolher o que fazer no programa e o que fazer com os números
opção = int # variável para conseguir voltar para as opções do menu, no último while

while menu != 5:
    numero1 = float(input('Arca:Informe o primeiro número:'))
    numero2 = float(input('Arca:Informe o segundo número:'))
    menu = 0 # zerei a variável menu pois quando voltava para esse while, o menu estava com o valor 4, o que não permitia ele descer novamente para o segundo while
    while menu != 4 and menu != 5: # caso o usuário escolha 4 ele volta para o while de cima, caso escolha cinco, ele volta tambem para o while de cima, mas já que o while de cima fecha quando o menu tem o valor 5 então logo os dois se fecham!
        opção = 0 #zerei a variável opção pois quando voltava para esse while, a opção estava com o valor 1, o que não permitia ele descer novamente para o segundo while
        menu = int(input('Arca:Escolha a opção desejada:'
                         '\n[ 1 ] somar'
                         '\n[ 2 ] multiplicar'
                         '\n[ 3 ] maior'
                         '\n[ 4 ] novos números'
                         '\n[ 5 ] sair do programa'
                         '\nArca: Escolha:'))
        print('============================')
        while opção != 1: # se escolherem a opção 1, ele fecha e volta para o while de cima

            if menu == 1:
                resultado = numero1 + numero2 # o resultado guardará o valor final
                print('Arca:A soma dos números:'
                      '\n{}{}{} + {}{}{} = {}{}{}'
                      f'\n============================'.format(cores["azul"],numero1,cores["limpa"],cores["vermelho"],numero2,cores["limpa"],cores["verde"],resultado,cores["limpa"]))
            if menu == 2:
                resultado = numero1 * numero2
                print('Arca:A multiplicação dos números:'
                      '\n{}{}{} X {}{}{} = {}{}{}'
                      f'\n============================'.format(cores["azul"],numero1,cores["limpa"],cores["vermelho"],numero2,cores["limpa"],cores["verde"],resultado,cores["limpa"]))
            if menu == 3:
                if numero1 > numero2:
                    resultado = numero1
                elif numero1 < numero2:
                    resultado = numero2
                else:
                    print('Arca:Os números possuem os mesmos valores! não a número maior!')
                print('Arca: O maior número é o {}{}{}'
                      f'\n============================'.format(cores["verde"],resultado,cores["limpa"]))

            opção = int(input('Arca: Deseja voltar ao menu?'
                  '\n[1] Sim'
                  '\n[2] Não'
                  '\n============================'))

print('Arca:Programa finalizado!')