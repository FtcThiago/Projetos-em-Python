#DESAFIO 045

"""045 Faça um programa que faça o computador jogar JOKENPÔ com você!"""

#Dê uma olhada no código do guanabara, foi bem mais simples que o meu e funcinou!não vou mudar o meu pq é meu
#raciocínio ainda, no entanto aprender novos métodos e mais simples é necessário


import emoji,time
from random import choice


jokempoUsuario = int(input('Arca:Informe o número desejado:'
                '\n1°Tesoura-->'
                '\n2°Pedra-->'
                '\n3°Papel-->'
                '\nInforme:'))


listaJokenpoPc = ['Tesoura', 'Pedra', 'Papel']#lista para que mais a frente o pc possa escolher entre tais parâmetros
listaEmoji = [emoji.emojize(":victory_hand:"), emoji.emojize(":raised_fist:"), emoji.emojize(":hand_with_fingers_splayed:")]
#Uma lista das figuras do emoji, para que eu não ficasse digitando denovo e denovo




jokenpoPc = choice(listaJokenpoPc) # comando para a Arca(maquina) escolher entre os parâmetros da listaJokenpoPc
status = ['Ganhou!', 'Perdeu!', 'Empate!']
statu = str
emojiPc = str
emojiUs = str
#A váriavel statu recebera mais a frente a lista status
#emojiPc e emojiUs, são variáveis para receber os parâmetros da listaEmoji


if jokempoUsuario == 1:
    emojiUs = listaEmoji[0]
elif jokempoUsuario == 2:
    emojiUs = listaEmoji[1]
elif jokempoUsuario == 3:
    emojiUs = listaEmoji[2]
else:
    print('Arca:Escolha inválida, escolha um número entre 1 e 3')
#Condição para saber se o usuário escolheu entre tesoura, pedra ou papel e coloca o emoji devido nas variavei emojiUs


if jokenpoPc == listaJokenpoPc[0]:
    emojiPc = listaEmoji[0]
elif jokenpoPc == listaJokenpoPc[1]:
    emojiPc = listaEmoji[1]
elif jokenpoPc == listaJokenpoPc[2]:
    emojiPc = listaEmoji[2]
#Condição para saber se a Arca(maquina) escolheu entre tesoura, pedra ou papel e coloca o emoji devido nas variavei emojiPc


print('Arca:JO')
time.sleep(1)
print('Arca:KÊN')
time.sleep(1)
print('Arca:PO')
time.sleep(1)
if jokenpoPc == listaJokenpoPc[0] and jokempoUsuario == 3 or jokenpoPc == listaJokenpoPc[1] and jokempoUsuario == 1 or jokenpoPc == listaJokenpoPc[2] and jokempoUsuario == 2:
    statu = status[1]
elif jokenpoPc == listaJokenpoPc[0] and jokempoUsuario == 2 or jokenpoPc == listaJokenpoPc[1] and jokempoUsuario == 3 or jokenpoPc == listaJokenpoPc[2] and jokempoUsuario == 1:
    statu = status[0]
elif jokenpoPc == listaJokenpoPc[0] and jokempoUsuario == 1 or jokenpoPc == listaJokenpoPc[1] and jokempoUsuario == 2 or jokenpoPc == listaJokenpoPc[2] and jokempoUsuario == 3:
    statu = status[2]
else:
    print('Dados inválidos!')
#Condição para saber quem ganhou, se a Arca ou o Usuário


print(20*'-=')

print(f'Sua escolha foi o número {jokempoUsuario} de acordo com a tabela'
      '\n1°Tesoura'
      '\n2°Pedra'
      '\n3°Papel')
print(f'Escolha da Arca:{jokenpoPc}')
print(20*'-=')

print(statu)
print(f'Arca:{emojiPc} x voce:{emojiUs}')
print(20*'-=')
#Por fim, aqui estará o resultado de quem ganhou e os devidos emojis das escolhas feitas
