#DESAFIO 035

#035 Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

import emoji

reta1 = float(input('Arca:Informe o tamanho da primeira reta:'))
reta2 = float(input('Arca:Informe o tamanho da segunda reta:'))
reta3 = float(input('Arca:Informe o tamanho da terceira reta:'))

valor1 = bool((abs(reta2-reta3)) < reta1 < (abs(reta2+reta3)))
valor2 = bool((abs(reta1-reta3)) < reta2 < (abs(reta1+reta3)))
valor3 = bool((abs(reta1-reta2)) < reta3 < (abs(reta1+reta2)))

if valor1==True or valor2==True or valor3==True:
    print(f'Arca:Os comprimentos da sua reta obedecem a regra para formar um Triangulo.{emoji.emojize(":red_triangle_pointed_up:")}')
else:
    print(f'Arca:Os valores informados não obedecem a regra para montar um triangulo{emoji.emojize(":exclamation_question_mark:")}')