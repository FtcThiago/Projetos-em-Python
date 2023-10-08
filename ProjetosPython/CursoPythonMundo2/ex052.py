"""Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um
número primo."""

#Demorei por demais para fazer esse exercício! Deus abençou e consegui hehe! coisa boa.
numero = int(input('Arca:digite um número inteiro acima de 1:'))

lista = []
mult= 0
for c in range(2, numero+1):
    if numero%c == 0:
        mult = mult + 1

if mult == 1:
    print('É primo!')
else:
    print('Não é Primo')


#-----------------------------------------
#Jeito do professor guanabara

num = int(input('Digite um número:'))
tot = 0 # uma variável para saber por quantos números o número escolhido é divisível


for c in range(1, num+1): # do número 1 até o número escolhido, assim conseguimos fazer as divisões com todos os números deis do um até o número escolhido e conseguimos vê por quantos números ele é divisível
    if num%c == 0:  # se o resto do 'num' dividido por 'c' for 0 então ele ficará azul, senão ele ficará normal
        print('\033[34m', end='') # comando de cor e o end para substituir a quebra de linha
        tot += 1
    else:
        print('\033[31m', end='') # ele ficara azul se for divisivel e vermelho se não for

    print('{}'.format(c), end=' ')# Aqui mostramos os números! os números ficam azul ou vermelho pelo fato de as cores serem escolhidas nos if antes de aparecerem os números da variável c

print(f'\n\033[mO Número {num} é divisível por {tot} números ') #Aqui fechamos o comando de cores no \033[m
if tot > 2:
         print('Por isso não é Primo')
else:
          print('Por isso é Primo')

