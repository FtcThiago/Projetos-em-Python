#Desafio 044

"""Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros"""

print('{:=^40}'.format('Lojas Arca'))

produto = float(input('Arca:Informe o preço do Produto: R$'))
condicaoPagamento = int(input('Arca:Escolha entre 1 a 4 de acordo com o tipo de pagamento desejado:'
                               '\n[1°] Dinheiro/Cheque '
                              ' \n[2°] À vista no cartão '
                              ' \n[3°] Até 2x no cartão '
                              ' \n[4°] 3x ou mais no cartão '
                              ' \nInforme:'))

tipos = ['Dinheiro,com desconto de 10%', 'A vista no cartão, com desconto de 5%', 'Em até 2x no cartão',
         '3x ou mais no cartão, com Juros de 20%']
escolha = str




if condicaoPagamento == 1:
    escolha = tipos[0]
    produto = (produto-(produto*(10/100)))
elif condicaoPagamento == 2:


    escolha = tipos[1]
    produto = (produto-(produto*(5/100)))
elif condicaoPagamento == 3:

    escolha = tipos[2]
    produto = produto

    parcela = 2


elif condicaoPagamento == 4:
    escolha = tipos[3]
    produto = produto + (produto * (20 / 100))

    print(20 * '-')
    parcela = int((input(f'Arca:Quantas vezes deseja parcelar?escolha de acordo com o número nos parênteses'
                         f'\n[3] 3x no cartão: {produto / 3:.2f}'
                         f'\n[4] 4x no cartão: {produto / 4:.2f}'
                         f'\n[5] 5x no cartão: {produto / 5:.2f}'
                         f'\n[6] 6x no cartão: {produto / 6:.2f}'
                         f'\n[7] 7x no cartão: {produto / 7:.2f}'
                         f'\n[8] 8x no cartão: {produto / 8:.2f}'
                         f'\n[9] 9x no cartão: {produto / 9:.2f}'
                         f'\n[10] 10x no cartão: {produto / 10:.2f}'
                         f'\nInforme:')))
    if parcela < 3 or parcela > 10:
        print(20*'-')
        print('Opção inválida')
        print(20*'-')
        exit()


else :
    print(20*'-')
    print('Condição de pagamento inválida!')
    print(20*'-')
    exit()



#A partir desse if, é a condição das frases, se escolherem parcela até 2x cai no primerio elif abaixo, se escolherem
# de 3x ou mais cair no if, se escolherem á vista ou á vista no cartão, cai no else
if condicaoPagamento == 4:
    print(20 * '-')
    print(f'Arca: O tipo de pagamento escolhido foi {escolha}!'
          f'\nArca: Sua compra será parcelada em {parcela}X de R${produto/parcela:.2f} '
          f'\nArca: O preço final com juros:R$ {produto:.2f}   ')
    print(20 * '-')

elif condicaoPagamento == 3:
    print(20 * '-')
    print(f'Arca: O tipo de pagamento escolhido foi {escolha}!'
          f'\nArca: Sua compra será parcelada em {parcela}X de R${produto/parcela:.2f} '
          f'\nArca: O preço final :R$ {produto:.2f}   ')
    print(20 * '-')

else:
    print(20*'-')
    print(f'Arca: O tipo de pagamento escolhido foi {escolha}!'
      f'\nArca: O preço final:R$ {produto:.2f}   ')
    print(20*'-')