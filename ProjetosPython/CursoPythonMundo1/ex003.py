print('Desafio 003')
msg = input('Digite algo:')
n = 5.5

cores = {'limpe': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'roxo': '\033[35m'}

print('{}{}{} é:'.format(cores['azul'], msg, cores['limpe']),
      '\nUm número:', msg.isnumeric(),
      "\né alfabético:", msg.isalpha(),
      "\nUm alfanumérico:", msg.isalnum(),
      "\nEstá em maiscúla:", msg.isupper(),
      "\nEstá em minúscula:", msg.islower(),
      "\nEstá capitalizada:", msg.istitle(),#capitalizada é a letras maiscúlas e minúsculas.
      "\nSó tem espaços:", msg.isspace(),
      "\nO TIPO PRIMITIVO DESTE é:", type(n))
