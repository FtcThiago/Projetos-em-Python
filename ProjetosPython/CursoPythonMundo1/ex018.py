#DESAFIO 018

from math import sin,cos,tan,radians

#Variável
ângulo = float(input('Arca:Digite o ângulo que deseja:'))
sen = sin(radians(ângulo))
cos = cos(radians(ângulo))
tan = tan(radians(ângulo))

print(f'Arca:O ângulo recebido foi {ângulo} '
      f'\nArca:O seno do ângulo é:{sen:.2f}...'
      f'\nArca:O cosseno do ângulo é:{cos:.2f}...'
      f'\nArca:A tangente do ângulo é:{tan:.2f}...')