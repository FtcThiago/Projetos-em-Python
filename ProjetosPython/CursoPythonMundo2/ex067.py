""" Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para
cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. """



print('{:=^40}'.format('Tabuada'))


numero = 0
c = 0 # contador do programa; essa variável sera usada para fazer a conta da tabuada
while numero >= 0:

    numero = int(input('Arca:Informe o número da tabuada desejada. Informe um número negativo para sair!'
                       '\nDigite:'))
    print('{:=^40}'.format(''))

    if numero >= 0 :
        c = 0 # tive que zerar o contador, para que conseguisse voltar para o while denovo....
        while c < 10:
            c = c + 1 # a tabuada irá apenas até o dez! como é de costume.
            print(f'{numero} X {c} = {numero * c}') # não guardei o calculo em nenhuma variável!
    else:
        print('Arca:Encerrando programa!')



