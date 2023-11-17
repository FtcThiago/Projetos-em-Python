"""Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus
respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular."""

produtos = ('Notebook', 1500, 'Tablet', 1200, 'Celular', 1300, 'Xbox One', 1400, 'Controle xbox', 300,
            'Suporte p/ notebook', 250, )
c = 0
d = 0
print('{:=^40}'.format(''))
print('{:-^40}'.format('Listagem De Preço').upper())
print('{:=^40}'.format(''))

while c != 12:


    print('{:.<30}'.format(produtos[c]), end='')
    c = c+1
    print(f' R$ {produtos[c]:.2f}')
    c = c+1
print('{:=^40}'.format(''))


#Modo do professor guanabara:

print('{:=^40}'.format(''))
print('{:-^40}'.format('Listagem De Preço-Guanabara').upper())
print('{:=^40}'.format(''))
#
for pos in range(0,len(produtos)): #Começando do zero até o tamanho da tupla ( o len() mede o tamanho do valor da variável, nesse caso quantos valores tem na tupla)
     if pos%2 == 0: #Aqui fomos na ideia, de que colocamos na tupla os produtos nas posições pares e os preços nas posições ímpares;nesse caso, se a posição tal dividido por 2 tiver o resto 0,é par, logo é produto
         print('{:.<30}'.format(produtos[pos]),end='')
     else:#Aqui estará o preço dos produtos
         print(f'R$ {produtos[pos]:.2f}')





#Meus Testes para achar a minha solução:
    # print(produtos[c + d], '{:.^20}'.format(''), produtos[c +1])
    # c = c+1
    # d = d+1
    # print(produtos[c], '{:.^20}'.format(''), produtos[c+1])
    # c = c + 2
    # print(produtos[c], '{:.^20}'.format(''), produtos[c + 1])
    # c = c + 2
    # print(produtos[c], '{:.^20}'.format(''), produtos[c + 1])
    # c = c + 2
    # print(produtos[c], '{:.^20}'.format(''), produtos[c + 1])
    # c = c + 2
    # print(produtos[c], '{:.^20}'.format(''), produtos[c + 1])


