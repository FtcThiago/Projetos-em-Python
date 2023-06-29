print('DESAFIO 015')
#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa
# R$60 por dia e R$0,15 por Km rodado.


print('-----------------------------------------------------------------'
      'Arca:Calculando o preço do Aluguel de carros'
      '-----------------------------------------------------------------')

print('-----informe as informações do carro-----')
dias = int(input('Informe a quantidade de dias utilizados: '))
km = float(input('Informe a quantidade de Km rodados:'))
preçoPagar=(dias*60)+(km*0.15)

print('Analisando quantidade de dias.......\nAnalisando quantidade de Km......\nCálculando o preço a ser pago')
print('Arca:valor por dia: R$60....valor por Km: R$:0,15')
print(f'Arca:O preço a pagar é: R$:{preçoPagar:.2f}')