"""Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual
foi o maior e o menor peso lidos."""

# Demorei muito para fazer este exercícios!Mas graças a Deus consegui!
# Eu tive que pesquisar na net para resolver! No entanto eu sabia exatamente o que estava procurando!
# e saber que eu sei como resolver, e entre tantas informações saber exatamente aonde ir,
# isso sim, me livra da culpa de ir pesquisar na internet.


print('{:^40}{:=^40}{:^40}'.format('Maior e Menor Peso(Kg)', 'Luta', 'Competiçao de luta'))



maior = 0  # variavel para receber o maior valor digitado de peso
menor = 0  # variavel para receber o menor valor digitado de peso
lista = [] # Essa lista será usada para receber os valores de peso

for c in range(1, 5+1):
     lista.append(float(input(f'Arca:Informe o peso(kg) do {c}° competidor:'))) # Aqui temos o comando append que joga na lista os valores de peso recebido




print(20*'=')
print(f'Arca: O maior peso foi de {max(lista)} Kg'
      f'\nArca: O menor peso foi de {min(lista)} kg') # temos o comando min() e max(), sendo o primeiro para devolver o maior valor da lista, e o segundo para devolver o menor valor.
print(20*'=')




# JEITO DO PROFESSOR(O QUAL EU NÃO PENSEI)
print('\n\n\nApartir daqui, é o programa copiado do professor Guanabara\n')

maiorp = 0
manorp = 0
for p in range(1, 6):
    pesop = float(input(f'Informe o peso do {p} competidor:'))
    if p == 1: # esse if basicamente é para o primeiro valor! quando o primeiro valor for informado, tanto o maiorp e o menorp devem recebe-lo, e só depois de cada variável ter um valor, que vai decidir se os outros valores digitados vão substituir esse primeiro valor
        maiorp = pesop
        menorp = pesop
    else:
        if pesop >maiorp:
            maiorp = pesop
        if pesop < menorp:
            menorp = pesop

print(20*'=')
print(f'Arca: O maior peso foi de {maiorp} Kg'
      f'\nArca: O menor peso foi de {menorp} kg')
print(20*'=')