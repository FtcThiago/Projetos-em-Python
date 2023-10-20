"""Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. """


print('{:=^40}'.format('Idade e Sexo dos Usuários'))


idade = maior = homens = mulheres = 0  #idade -> receber idade; maior -> receber maiores de 18 anos; homens -> receber todos os de sexo masculino; mulheres -> receber todas as de sexo feminino que tem menos de 20 anos
sexo = ''
escolha = str




print('{:=^40}'.format(''))
print('{:^40}'.format('CADASTRO'))
print('{:=^40}'.format(''))

while escolha != 'N': # Se o usuário escolher a opção de sair, o while fecha.
    sexo = escolha = '' # Zerei essas variáveis para que os whiles que as utilizam possam continuar funcionando, já que quando se utiliza o while, elas são preenchidas com as opções que o usuário escolheu anteriormente
    idade = int(input('Arca:Informe sua idade:'))

    if idade >= 18:
        maior = maior + 1

    while sexo != 'F' and sexo !='M': # Esse while basicamente é para que caso o usuário digite errado, ele não saia daqui até digitar certo.
        sexo = str(input('Arca:Informe seu sexo:'
                     '\n[M]Masculino'
                     '\n[F]Feminino')).upper()[0]


        if sexo != 'M' and  sexo !='F': #Função caso o usuário digite errado
            print('{:=^40}'.format(''))
            print('Arca:Opção inválida ')
            print('{:=^40}'.format(''))

        if sexo == 'M':
            homens = homens  + 1
        if sexo == 'F' and idade < 20:
            mulheres = mulheres + 1


    while escolha != 'S' and escolha!='N':
        escolha = str(input('Arca:Deseja continuar?'
                    '\n[S]Sim'
                    '\n[N]Não')).upper()[0] # O upper() é para deixar as letras maisculas; e o [0] é para que seja considerada só a primeira letra informada!

print('{:=^40}'.format('Resultados'))
print(f'Arca: Maiores de 18 anos:{maior} '
      f'\nArca: Homens cadastrados:{homens}'
      f'\nArca: Mulheres menores de 20 anos :{mulheres}')
