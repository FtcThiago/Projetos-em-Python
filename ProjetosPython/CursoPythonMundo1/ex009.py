print('DESAFIO 09')

print('Tabuada de Multiplicação')#Aqui vou fazer tabuada de Multiplicação(ou qualquer outra,trocando o operando).

numero = int(input('Informe o número da tabuada desejada:'))
n = int(1)
print('_' * 12)
while (n<=10):

      print('{} X {:2}={}'.format(numero, n, numero*n)) #Aqui eu coloquei {:2} para todos eles ficarem com dois digitos
      n = n + 1
else:
      print('_' * 12)
      print('O loop foi encerrado com suceso!')








