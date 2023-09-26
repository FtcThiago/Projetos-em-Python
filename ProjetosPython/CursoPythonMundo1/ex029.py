#DESAFIO 029


#029 Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h,mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

veloc = float(input('Arca:Informe a velocidade do carro, agente:'))
multa = (veloc - 80) * 7
if veloc > 80:
    print(f'Arca:O motorista ultrapassou a velocidade permitida de 80Km/h;Será multado!'
          f'\nArca:Velocidade do motorista:{veloc:.0f}Km/h'
          f'\nArca:O valor da multa é:R${multa:.2f}')
else:
    print("Arca:Muito bem!motorista liberado.Dentro da velocidade exigida! ")
