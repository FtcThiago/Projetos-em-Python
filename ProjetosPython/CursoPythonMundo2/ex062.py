'''Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais
alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''

print('{:=^60}'.format('Progressão Artimética com While-Melhorada'))

cores = {'limpa':'\033[m',
        'verde':'\033[32m' ,
        'azul':'\033[34m',
        'vermelho':'\033[31m'}


termo = int(input('Arca:Informe o primeiro termo da PA:'))
razão = int(input('Arca:Informe a razão da PA:'))
termoOriginal = termo # variável para guarda o termo original digitado pelo usuário, levando em conta que o termo será modificado durante o processo
quantidadeTermos = int  # Variável para receber a quantidade de termos a mais que o usuário vai desejar
c = 1 # variável apenas para ser um contador

while quantidadeTermos != 0:
    while c != 10:

        print('{}{}{},'.format(cores['azul'],termo, cores['limpa']), end='') # Aqui estamos apresentando os 10 primerios termos
        termo = termo + razão # aqui está a forma que eu achei para achar a progressão aritmética de acordo com o primeiro termo e razão
        c = c+1 # contador recebendo valor, para que o while consiga acabar

    while quantidadeTermos != 0 :
        print('\n{:=^60}'.format(''))
        quantidadeTermos = int(input('\nArca:Deseja mostrar mais termos?'
                                '\nArca:Digite quantos mais deseja'
                                '\nArca:Ou digite {}0{} para sair'
                                '\nArca:Digite:'.format(cores['vermelho'], cores['limpa'])))
        print('{:=^10}'.format(''))
        if quantidadeTermos != 0 : # se o usuário escolher um número diferente de 0( que no caso, o 0 fecha o programa, ele entra no if)
            c = 0 # tive que zerar o contador, para que ele pudesse mostrar todos os termos deis do primeiro digitado,até a quantidade desejada pelo usuário, digita e guardada na variável quantidadeTermos
            while c !=quantidadeTermos:
                print('{}{}{},'.format(cores['azul'], termo, cores['limpa']), end='')
                termo = termo + razão
                c = c + 1
print('{}Acabou!{}'.format(cores['verde'],cores['limpa'])) # To tentando colocar cor em todo meu programa


