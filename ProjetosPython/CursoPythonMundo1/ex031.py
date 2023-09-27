#DESAFIO 031

#031 Desenvolva um programa que pergunte a distância de uma viagem em Km.Calcule o preço da passagem,cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas

dist = float(input('Arca:Informe a distância da viagem em Km/h:'))

if dist <= 200:
    print(f'Arca:Preço da passagem:R${dist * 0.50:.2f}')
else:
    print(f'Arca:Preço da passagem:R${dist * 0.45:.2f}')