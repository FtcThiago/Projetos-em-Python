print('DESAFIO 008')

cores = {'limpe': '\033[m',
         'branco': '\033[30m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'roxo': '\033[35m',
         'verde': '\033[32m',
         'ciano': '\033[36m'}


print('Conversão de metros para centímetros e milímetros')
metro = float(input('Informe o valor em Metro:'))

print('O Valor informado:{}'
      '\nO valor em milímetros(mm):{}{}{}'
      '\nO valor em Centímetros(cm):{}{}{}'
      '\nO valor em Decímetro(dm):{}{}{}'
      '\nO valor em Quilômetro(KM):{}{}{}'
      '\nO valor em Hectômetro(hm):{}{}{}'
      '\nO valor em Decâmetro(dam):{}{}{}'
      '\n'.format(cores['branco'], metro, cores['limpe'], cores['azul'], metro*1000, cores['limpe'], cores['vermelho'], metro*100, cores['limpe'],
                  cores['amarelo'], metro*10, cores['limpe'], cores['roxo'], metro/1000, cores['limpe'],cores['verde'], metro/100, cores['limpe'],
                  cores['ciano'], metro/10, cores['limpe']))
