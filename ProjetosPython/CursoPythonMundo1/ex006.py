print('DESAFIO 006')

cores = {'limpe': '\033[m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'branco': '\033[30m'}

n1 = int(input('Informe o número:'))
print('Infomação do Número {}{}{}'
      '\n O dobro:{}{}{}'
      '\n O triplo:{}{}{}'
      '\n Raiz Quadrada:{}{:.2f}{}'.format(cores['azul'], n1, cores['limpe'], cores['vermelho'], n1*2, cores['limpe'],
                                       cores['vermelho'], n1*3, cores['limpe'], cores['vermelho'], n1**(1/2), cores['limpe']))

