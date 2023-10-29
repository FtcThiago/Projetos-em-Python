""" Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. """

print('{:=^40}'.format('Compras de produtos'))

produto = nomeProdutoBarato = ''
preço = gasto = prodBarato  = c = 0
maisDeMil = escolha = 0

produto = str(input('Arca:Informe o nome do produto:'))
preço = float(input('Arca:Informe o preço do produto! R$:'))

while True:
    escolha = 0
    escolha = int(input('Arca:Deseja continuar?'
                  '\n[1] SIM'
                  '\n[2] NÃO:'))
    gasto = gasto + preço
    c = c+1
    if preço > 1000:
        maisDeMil = maisDeMil + 1
    if c == 1 or preço < prodBarato:
        prodBarato = preço
        nomeProdutoBarato = produto


    if escolha == 1:
        print('{:=^40}'.format(''))
        produto = str(input('Arca:Informe o nome do produto:'))
        preço = float(input('Arca:Informe o preço do produto! R$:'))
    if escolha == 2:
        break


print('{:=^40}'.format('Informações dos produtos'))
print(f'Arca: O valor total gasto é de R${gasto:.2f}')
print(f'Arca: Cerca de {maisDeMil} produtos custaram mais de R$1000')
print(f'Arca: O produto mais barato é o/a {nomeProdutoBarato} com o preço de R${prodBarato:.2f}')
