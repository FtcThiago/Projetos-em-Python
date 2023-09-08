#DESAFIO 027

#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = input('Arca:Informe o seu nome completo:').strip().upper()
nome = n.split() #lembre que o split() está 'cortando' as palavras, exemplo: Thiago felix t chaves-----> [0-Thiago] [1-felix] [2-t] [3-chaves]

print(f'Arca: a primeira parte do nome informado é: {nome[0]}'
      f'\nArca:a última parte do nome informado é: {nome[len(nome)-1]}') #assim nome[len(nome)] ele consegue mostrar a ultima parte do nome