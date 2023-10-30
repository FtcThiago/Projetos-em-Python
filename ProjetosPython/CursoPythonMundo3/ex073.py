""" Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense."""

print('{:=^40}'.format('BRASILEIRÃO SÉRIE B'))


colocados = ('Cruzeiro', 'Vasco', 'Bahia', 'Grêmio', 'Tombense', 'Sport', 'Londrina', 'Novorizontino', 'Sampaio Corrêa',
             'CRB', 'Criciúma', 'Brusque', 'Chapecoense', 'Ponte Preta', 'Operário-PR', 'Ituano', 'CSA', 'Náutico',
             'Guarani', 'Vila Nova')

print(f'Arca: Os cinco primeiros colocados foram: {colocados[0:5]}')#Vai mostrar os valores contidos e começando nas posições 0 até 5 dentro da tupla
print('{:=^40}'.format(''))
print(f'Arca: Os últimos quatro colocados foram:{colocados[-4:]}')#Vai mostrar os valores contidos e começando nas posições -4(menos quatro é a posição começando do 4° numero antes do final) até o ultimo número, por isso deixei a posição vazia.
print('{:=^40}'.format(''))
print(f'Arca: Todos os Times em Ordem alfabética: {sorted(colocados)}') # o comando sorted() cuida de colocar em ordem alfabetica e numerica os valores contidos na tupla
print('{:=^40}'.format(''))
print(f'Arca: O time {colocados[colocados.index("Chapecoense")]} está na posição {colocados.index("Chapecoense")}') # usei o comando index para achar o nome da chapecoense e descobrir sua posição, e usei sua posição para mostra na tela tanto o nome dentro da posição , quanto a propria posição respectivamente

