#DESAFIO 036

"""Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
 Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não
 pode exceder 30% do salário ou então o empréstimo será negado."""

print(20*'-')
casa = float(input('Arca:Por favor, informe o valor da casa: R$'))
salarioComprador = float(input('Arca:Agora informe o salário do comprador: R$'))
anos = int(input('Arca:Por fim, por favor, informe em quantos anos deseja pagar a casa:'))
print(20*'-')

prestacao = casa/(anos*12)
porcentagem = salarioComprador*(30/100)

if prestacao > salarioComprador*(30/100):
    print('Arca:Infelizmene você não pode financiar essa casa. Analisando, não vejo meios "sólidos" de você conseguir paga-la')
    print('Arca:Emprestimo negado!'
          f'\nO valor da Prestação seria de R$ {prestacao:.2f} por {anos} anos')
else:
    print('Arca:Emprestimo aceito!'
          f'\nO valor da Prestação será de R${prestacao:.2f} por {anos} anos')