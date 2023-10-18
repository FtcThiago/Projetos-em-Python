'''Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da
execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa
deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''


print('{:=^60}'.format('Média,maior e menor valor entre números!'))



c = 0 #variável para decidir se deseja continuar no programa ou não
quant = 0  #variável que ajuda na decisão de quem é o maior ou menor número! e ajuda na média final.
soma = menor = maior = 0
print('Arca: Informe um número inteiro!')

while c != 2:

    numero = int(input('Arca:Digite:'))
    quant = quant + 1
    
    print('{:=^10}'.format(''))
    c = int(input('Arca:Deseja continuar?'
                  '\n[1] Sim'
                  '\n[2] Não'
                  '\nDigite:'))
    print('{:=^10}'.format(''))

    soma = soma + numero
    
    if quant == 1: # Aqui as duas variáveis Maior e Menor recebem o primeiro valor digitado pelo usuário
        maior = numero
        menor = numero

    if numero > maior: #Decisão para variável maior receber maior valor digitado
        maior = numero

    if numero < menor: #Decisão para variável menor receber o menor valor digitado
        menor = numero


media = soma / quant
print(f'Arca:Você digitou {i} valores e a Média de todos os números é {media}')

if maior == menor :
    print(f'Arca: Não a número maior ou menor! Ambos são iguais! tendo o número {maior}')
else:
    print(f'\nArca: Sendo o MAIOR número o {maior}'
        f'\nArca: E o MENOR número o {menor}')