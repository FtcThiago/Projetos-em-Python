"""Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela."""

aluno = {}#Criando Dicionário

aluno['nome'] = str(input('Arca:Informe o nome do aluno:'))#Criando Key recebendo como nome o nome e recebendo como valor o que o usuário digitar.
aluno['nota1'] = float(input('Arca:Informe a primeria nota:'))#Criando Key recebendo como nome nota1 e recebendo como valor o que o usuário digitar.
aluno['nota2'] = float(input('Arca:Informe a segunda nota:'))#Criando Key recebendo como nome nota2 e recebendo como valor o que o usuário digitar.
aluno['media'] = (aluno['nota1'] + aluno['nota2'])/2 #Criando Key recebendo como nome media e recebendo como valor o calculo entre os valores dentro da key nota1 e nota2.

if aluno['media'] > 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] <= 6.9 and aluno['media'] >= 6:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

print('-='*30)
for k,v in aluno.items():#O item() é usado para que possamos acessar do dicionário tanto as keys como os valores.e as variáveis k e v recebem respectivamente Keys e valores.
    print(f'{k.title()}: {v}')#title() é para deixar a primeira letra do nome maiscula.
