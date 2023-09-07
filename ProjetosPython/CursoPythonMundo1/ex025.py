#DESAFIO 025

#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Arca:Infomre o seu nome:').strip().upper()


if "SILVA" in nome:
    print('Arca:Econtramos Silva em seu nome, por favor direcione-se aqueles guardas.você está sendo submetido a uma '
          'investigação policial.')
else:
    print('Arca:Nome checado com sucesso,não contem o nome Silva.permição para prosseguir!')


#nome = input('Arca:Infomre o seu nome:').strip().upper()
#print(f'Seu nome tem Silva? {"SILVA" in nome}')


