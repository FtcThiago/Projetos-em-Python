#DESAFIO 022

#Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas e
#minúsculas. - Quantas letras ao todo sem considerar espaços. - Quantas letras tem o primeiro nome.

nome = input('Arca:Informe seu nome:').strip() #o stripp vai lançar fora os espaços inuteis no inicio e no final
separa=nome.split()
print(f'O nome informado foi: {nome} '
      f'\nO nome informado em Letras Maisculas: {nome.upper()}'
      f'\nO nome informado em Letras Minusculas: {nome.lower()}'
      f'\nQuantas letras do nome sem considerar os espaços: {len(nome)-nome.count(" ")}'
      f'\nO seu primeiro nome é {separa[0]}---Quantas letras tem o primeiro nome:{len(separa[0])}')
      
      
      #Outro exemplo em baixo
      # f'\nQuantas letras tem o primeiro nome:{nome.find(" ")} ')#Aqui usamos o find colocando como parametro o espaço, fazendo assim contar todo o total de letras antes do primeiro espaço