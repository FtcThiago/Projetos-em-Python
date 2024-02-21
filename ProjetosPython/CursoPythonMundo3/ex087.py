""""Aprimore o desafio anterior, mostrando no final:
    A) A soma de todos os valores pares digitados.
    B) A soma dos valores da terceira coluna.
    C) O maior valor da segunda linha."""


matriz = [[0,0,0],[0,0,0,],[0,0,0,], [0,0,0,]] #Criando listas dentro de listas
pares = coluna = 0

for c in range(0, 3):
    for i in range(0, 3):
        matriz[c][i] = int(input(f'Arca:Informe o número para [{c},{i}]')) #Recebendo os valores digitados de acordo com a posiçaõ determinada



print('-='*60)

for c in range(0,3):
    print()

    coluna = coluna + matriz[c][2] # Variável coluna para receber a soma dos valores da ultima coluna.


    for i in range(0,3):
        print(f'[{matriz[c][i]:^5}]', end='')

        if matriz[c][i] % 2 == 0:#Condição para vê se o número é par
            pares = pares + matriz[c][i] #Variável para receber a soma de todos os números pares.


print()
print('-='*30)
print(f'A soma de todos os pares: {pares}')
print(f'A soma da ultima coluna da matriz: {coluna}')
print(f'O maior valor da segunda linha: {max(matriz[1])}')#Condição achar o maior valor entre os números na posição 1 da matriz.