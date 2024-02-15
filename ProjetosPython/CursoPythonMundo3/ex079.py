""" Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final,
serão exibidos todos os valores únicos digitados, em ordem crescente. """


print('{:=^40}'.format('Cadastro de números em uma lista'))

numeros = list()
numero = 0
opção= ''
repetidos = 0



while True :
    numero = (int(input(f'Arca:Informe o  número:')))


    if numero in numeros:
        print('Arca:Número repetido! Não vou considerar....')
    else:
        print('Adicionado com sucesso')
        numeros.append(numero)



    while True:
        opção = input('Arca:Quer continuar? [S/N]')
        if opção != 'N' and opção != 'n' and opção != 'S' and opção != 's':
            print('Arca:Opção inválida!Informe novamente.')
        else:
            break

    if opção in 'Nn':
        break


print('='*40)
print(f'Arca:Os números digitados foram {sorted(numeros)}! desconsiderando os repetidos.')
