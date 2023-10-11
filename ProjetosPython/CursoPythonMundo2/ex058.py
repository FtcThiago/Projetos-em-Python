'''Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre
0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
necessários para vencer.'''


import random, time

print('{:=^84}'.format('Adivinhando Números'))

print('Arca:Irei escolher um número entre 0 e 10! Tente adivinhar que número irei escolher.')



numero = int
palpite = 0 # variável para somar quantas vezes o usuário errou antes de acertar
numeroArca = random.randrange(0,10)  #  numeroArca é a variavel que vai guardar o número que o pc vai escolher! Arca é o nome ficticio que dei a ele; random.randrange(0,10) é o comando para o pc escolher aleatoriamente um número entre 0 e 10
while numero != numeroArca:
    numero = int(input('Arca:Adivinhe o número:'))


    if numero > 10 or numero < 0:  # se o numero for menor que 0 ou maior que 10 ; função caso o usuário escolha uma opção inválida
        print('Opção inválida'
              '\nEscolha entre 0 e 10')
        print('==========')
        palpite = palpite + 1
    elif numero != numeroArca: # função caso o usuário escolha a opção errada, que não seja o número da Arca(pc)
        if numero > numeroArca:
            print('Arca:Errado!Menos') # ideia de menos e mais;peguei do guanabara
        if numero < numeroArca:
            print('Arca:Errado!Mais')
    print('==========')
    palpite = palpite + 1



print(f'===================='
      f'\nArca:Você acertou! com um total de {palpite} erros ou palpites.'
      f'\nArca: Eu escolhi o número {numeroArca}!')