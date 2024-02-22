"""Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
de cada aluno individualmente."""

alunos = []
cont = media = 0
opçao = " "

#================================================================
while True:

    alunos.append([])#Criando lista dentro da lista alunos
    alunos[cont].append(str(input('Arca:Informe seu nome:')).title()) #condição para receber os valores digitados pelo usuário dentro lista dentro da lista alunos
    alunos[cont].append(float(input('1° nota:')))
    alunos[cont].append(float(input('2° nota:')))
    cont += 1

    opçao = 0
    while opçao != 'S' and opçao != 's' and opçao != 'N' and opçao != 'n' :#condição para a opção se deseja continuar ou não
        opçao = input('Arca:Deseja continuar? [S/N]')

        if opçao in 'SsNn':
            break
        else:
            print('Arca:Opção inválida')
    if opçao in 'Nn':
        break

#===================================================================
print('{:<4}{:<10}{:>8}'.format("N°",'Nome','Média')) #condições para organizar as palavra em ordem como texto
print('-='*30)
for c in range(0,len(alunos)):

    media = (alunos[c][1] + alunos[c][2])/2 #Cálculo da media
    print(f'{c:<4}{alunos[c][0]:<10}{media:>8.1f}',  end='') #Tabela dos nomes e notas dos alunos; c posição dos valores da lista; alunos[c][0] nome dos alunos; media media das notas.
    print()

#====================================================================
opçao = 0
print('-='*30)
while True:
    opçao = int(input('Mostrar nota de quais alunos?(999 interrompe)'
                      '\nDigite:'))

    if opçao > len(alunos) or opçao < 0:
        print('Arca:Opção inválida!')
    else:
        print(f'Arca: As notas de {alunos[opçao][0]} são [{alunos[opçao][1]}] e [{alunos[opçao][2]}]')
    print('-='*30)

    if opçao == 999:
        break
