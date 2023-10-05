"""Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos
 de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles."""

#Importações
import time, emoji



print('{:=^40}'.format('Fogos de Artifícios'))

print('Arca:Contagem regressiva em....')
for c in range(10, -1, -1):
    print(f'Arca:{c}')
    time.sleep(1)

print(f'{emoji.emojize(":party_popper:")}Arca:Feliz ano novo!{emoji.emojize(":sparkles:")}')
time.sleep(3)
print('\nArca:Nada irá mudar se você continuar fazendo as mesmas coisas!'
      '\nArca:Essa afirmação é relativa! Pois se desejas emagrecer e continuas a comer em excesso nada mudará.'
      '\nArca:Se desejas no entanto ter um bom corpo, será necessário continuar fazendo diariamente os mesmos exercícios para mudar seu corpo!')