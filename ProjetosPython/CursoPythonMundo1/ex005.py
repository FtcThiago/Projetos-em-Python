print('DESAFIO 005')


cores = {'limpe': '\033[m',
        'azul':'\033[34m',
        'vermelho': '\033[31m',
        'roxo': '\033[35m'}

n1 = int(input('Informe o Número:'))

print('O successor de {}{}{} é: {}{}{} e o seu antecessor é: {}{}{}'.format(cores['azul'], n1, cores['limpe'], cores['vermelho'],
                                                                            n1+1, cores['limpe'], cores['roxo'], n1-1, cores['limpe']))
